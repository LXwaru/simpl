"""empty message

Revision ID: 408cb1e000d4
Revises: d860e2345edb
Create Date: 2024-10-02 14:33:50.147880

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '408cb1e000d4'
down_revision: Union[str, None] = 'd860e2345edb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
