"""Creates UserHorse join table

Revision ID: afbf63b5e73e
Revises: 6607d1c18d9c
Create Date: 2023-10-06 07:18:25.307348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afbf63b5e73e'
down_revision = '6607d1c18d9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_horses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('horse_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['horse_id'], ['horses.id'], name=op.f('fk_users_horses_horse_id_horses')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_users_horses_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_horses')
    # ### end Alembic commands ###
