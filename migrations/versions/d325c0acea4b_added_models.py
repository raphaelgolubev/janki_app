"""added models

Revision ID: d325c0acea4b
Revises: 5c5c8eae4465
Create Date: 2024-09-05 00:18:04.633661

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd325c0acea4b'
down_revision: Union[str, None] = '5c5c8eae4465'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('answer', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('hashed_password', sa.String(), nullable=False))
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users', 'hashed_password')
    op.drop_table('profiles')
    op.drop_table('cards')
    # ### end Alembic commands ###
