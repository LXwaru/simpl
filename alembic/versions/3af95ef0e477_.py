"""empty message

Revision ID: 3af95ef0e477
Revises: 7ef20dc5d602
Create Date: 2024-09-17 13:50:34.267911

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3af95ef0e477'
down_revision: Union[str, None] = '7ef20dc5d602'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
