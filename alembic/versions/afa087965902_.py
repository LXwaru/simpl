"""empty message

Revision ID: afa087965902
Revises: 2a157bd535d4
Create Date: 2024-09-12 12:48:06.412484

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'afa087965902'
down_revision: Union[str, None] = '2a157bd535d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
