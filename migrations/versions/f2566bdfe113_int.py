"""'Int'

Revision ID: f2566bdfe113
Revises: 
Create Date: 2023-04-25 15:27:00.476288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2566bdfe113'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'station',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.create_foreign_key(None, 'user', 'location', ['station'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.alter_column('user', 'station',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    # ### end Alembic commands ###
