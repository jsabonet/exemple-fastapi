"""add foreing-key to posts table

Revision ID: 3344c05834ec
Revises: e6425ec01fc5
Create Date: 2024-12-05 14:42:10.389387

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3344c05834ec'
down_revision: Union[str, None] = 'e6425ec01fc5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'post_user_fk', 
        source_table="posts",
        referent_table="user",
        local_cols=['owner_id'],
        remote_cols=['id'],
        ondelete="CASCADE"
    )

def downgrade():
    op.drop_constraint('post_user_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
