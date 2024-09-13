"""empty message

Revision ID: 532a7614f6cf
Revises: cf8b98ce2a1b
Create Date: 2024-09-12 22:53:34.501685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '532a7614f6cf'
down_revision: Union[str, None] = 'cf8b98ce2a1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
