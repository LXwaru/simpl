"""empty message

Revision ID: a023f2ff93c0
Revises: e435c0fb4a8c
Create Date: 2024-10-02 13:56:53.167829

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a023f2ff93c0'
down_revision: Union[str, None] = 'e435c0fb4a8c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
