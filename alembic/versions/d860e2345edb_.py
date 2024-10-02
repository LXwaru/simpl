"""empty message

Revision ID: d860e2345edb
Revises: e2eb30e97cdd
Create Date: 2024-10-02 14:10:04.578117

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd860e2345edb'
down_revision: Union[str, None] = 'e2eb30e97cdd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
