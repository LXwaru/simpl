"""empty message

Revision ID: 33be7e5c9abe
Revises: 42a32fb94ebe
Create Date: 2024-09-17 15:31:57.499807

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33be7e5c9abe'
down_revision: Union[str, None] = '42a32fb94ebe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
