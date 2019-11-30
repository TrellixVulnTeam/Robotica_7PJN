"""empty message

Revision ID: 23c2619c2b6a
Revises: e3736ecedf6b
Create Date: 2019-11-24 13:18:41.043188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23c2619c2b6a'
down_revision = 'e3736ecedf6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Equipes', ['email'])
    op.create_unique_constraint(None, 'Equipes', ['site'])
    op.create_unique_constraint(None, 'Equipes', ['firstname'])
    op.create_unique_constraint(None, 'Equipes', ['lastname'])
    op.create_unique_constraint(None, 'Equipes', ['slogan'])
    op.drop_column('Equipes', 'name')
    op.drop_column('Equipes', 'professor')
    op.add_column('Pessoas', sa.Column('CPF', sa.String(), nullable=True))
    op.add_column('Pessoas', sa.Column('RG', sa.String(), nullable=True))
    op.add_column('Pessoas', sa.Column('Telefone', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'Pessoas', ['RG'])
    op.create_unique_constraint(None, 'Pessoas', ['CPF'])
    op.create_unique_constraint(None, 'Pessoas', ['Telefone'])
    op.drop_column('Pessoas', 'identificacao')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Pessoas', sa.Column('identificacao', sa.VARCHAR(), nullable=True))
    op.drop_constraint(None, 'Pessoas', type_='unique')
    op.drop_constraint(None, 'Pessoas', type_='unique')
    op.drop_constraint(None, 'Pessoas', type_='unique')
    op.drop_column('Pessoas', 'Telefone')
    op.drop_column('Pessoas', 'RG')
    op.drop_column('Pessoas', 'CPF')
    op.add_column('Equipes', sa.Column('professor', sa.VARCHAR(), nullable=True))
    op.add_column('Equipes', sa.Column('name', sa.VARCHAR(), nullable=True))
    op.drop_constraint(None, 'Equipes', type_='unique')
    op.drop_constraint(None, 'Equipes', type_='unique')
    op.drop_constraint(None, 'Equipes', type_='unique')
    op.drop_constraint(None, 'Equipes', type_='unique')
    op.drop_constraint(None, 'Equipes', type_='unique')
    # ### end Alembic commands ###
