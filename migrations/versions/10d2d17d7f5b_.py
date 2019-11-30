"""empty message

Revision ID: 10d2d17d7f5b
Revises: b1103453b191
Create Date: 2019-11-01 20:12:11.188720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10d2d17d7f5b'
down_revision = 'b1103453b191'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Equipes', sa.Column('firstname', sa.String(), nullable=True))
    op.add_column('Equipes', sa.Column('lastname', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'Equipes', ['site'])
    op.create_unique_constraint(None, 'Equipes', ['firstname'])
    op.create_unique_constraint(None, 'Equipes', ['lastname'])
    op.create_unique_constraint(None, 'Equipes', ['slogan'])
    op.create_unique_constraint(None, 'Equipes', ['email'])
    op.drop_column('Equipes', 'professor')
    op.drop_column('Equipes', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Equipes', sa.Column('name', sa.VARCHAR(), nullable=True))
    op.add_column('Equipes', sa.Column('professor', sa.VARCHAR(), nullable=True))
    op.drop_constraint(None, 'Equipes', type_='unique')
    op.drop_constraint(None, 'Equipes', type_='unique')
    op.drop_constraint(None, 'Equipes', type_='unique')
    op.drop_constraint(None, 'Equipes', type_='unique')
    op.drop_constraint(None, 'Equipes', type_='unique')
    op.drop_column('Equipes', 'lastname')
    op.drop_column('Equipes', 'firstname')
    # ### end Alembic commands ###
