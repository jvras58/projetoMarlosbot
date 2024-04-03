from sqlalchemy.orm import Mapped, mapped_column

from app.config.base_model import Base


class Users(Base):
    """
    Representa a tabela Users do bot no banco de dados.
    """

    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, name='id')
    user_id: Mapped[int] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=True)
