"""empty message

Revision ID: e2eb30e97cdd
Revises: a023f2ff93c0
Create Date: 2024-10-02 13:57:52.731695

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2eb30e97cdd'
down_revision: Union[str, None] = 'a023f2ff93c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
