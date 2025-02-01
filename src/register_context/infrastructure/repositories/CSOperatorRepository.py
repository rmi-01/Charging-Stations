# repository/user_repository.py
from src.register_context.domain.entities.csoperator import CSOperator
from src.register_context.domain.value_objects import Password
from src.register_context.domain.events.CSOperatorAlreadyExistEvent import CSOperatorAlreadyExistEvent
from sqlalchemy.orm import Session

class CSOperatorRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_csoperator_by_username(self, username: str) -> CSOperator:
        csoperator=self.session.query(CSOperator).filter(CSOperator.username == username).first()
        if csoperator:
            return CSOperatorAlreadyExistEvent(csoperator.username,csoperator.password,"CSOperator already exist")
        return csoperator

    def add_csoperator(self, csoperator: CSOperator):
        self.session.add(csoperator)
        self.session.commit()

    def signin_csoperator(self, username: str, password: str) -> CSOperator:
        return self.session.query(CSOperator).filter_by(username=username,password=password).first()
    
    def get_all_csoperators(self):
        return self.session.query(CSOperator).all()
    
    def update_csoperator(self, csoperator: CSOperator) -> CSOperator:
        updated_operator = self.session.merge(csoperator)
        self.session.commit()
        return updated_operator