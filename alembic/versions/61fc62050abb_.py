"""empty message

Revision ID: 61fc62050abb
Revises: 3af95ef0e477
Create Date: 2024-09-17 14:00:24.540891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61fc62050abb'
down_revision: Union[str, None] = '3af95ef0e477'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
