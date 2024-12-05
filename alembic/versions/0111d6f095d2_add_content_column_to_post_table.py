"""add content column to post table

Revision ID: 0111d6f095d2
Revises: cb0589538a73
Create Date: 2024-12-05 14:27:01.451996

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0111d6f095d2'
down_revision: Union[str, None] = 'cb0589538a73'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))

def downgrade():
    op.drop_column('posts', 'content')