"""empty message

Revision ID: a04e4688d32b
Revises: afa087965902
Create Date: 2024-09-12 14:50:16.590615

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a04e4688d32b'
down_revision: Union[str, None] = 'afa087965902'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
