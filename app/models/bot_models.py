from config.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column


class Config_bot(Base):
    """
    Representa a tabela configurações do bot no banco de dados.
    """

    __tablename__ = 'config'

    id: Mapped[int] = mapped_column(primary_key=True, name='id')
    enviar_everyone: Mapped[bool] = mapped_column(nullable=True)
    enviar_dm: Mapped[bool] = mapped_column(nullable=True)
    ids_ignorados: Mapped[str] = mapped_column(nullable=True)
    canal_checkpoint_id: Mapped[int] = mapped_column(nullable=True)
    canal_planilha_id: Mapped[int] = mapped_column(nullable=True)
    alerta_checkpoint_horario: Mapped[str] = mapped_column(nullable=True)
    verificar_checkpoint_horario: Mapped[str] = mapped_column(nullable=True)