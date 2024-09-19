"""empty message

Revision ID: e45e97e45ad7
Revises: 46691deaf7ec
Create Date: 2024-09-17 15:41:25.039336

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e45e97e45ad7'
down_revision: Union[str, None] = '46691deaf7ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
