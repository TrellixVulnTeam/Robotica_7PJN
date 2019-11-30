"""empty message

Revision ID: e3736ecedf6b
Revises: f2a49faa0485
Create Date: 2019-11-24 13:14:08.956645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3736ecedf6b'
down_revision = 'f2a49faa0485'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Equipes', ['firstname'])
    op.create_unique_constraint(None, 'Equipes', ['lastname'])
    op.create_unique_constraint(None, 'Equipes', ['slogan'])
    op.create_unique_constraint(None, 'Equipes', ['email'])
    op.create_unique_constraint(None, 'Equipes', ['site'])
    op.drop_column('Equipes', 'name')
    op.drop_column('Equipes', 'professor')
    op.add_column('Pessoas', sa.Column('CPF', sa.String(), nullable=True))
    op.add_column('Pessoas', sa.Column('RG', sa.String(), nullable=True))
    op.add_column('Pessoas', sa.Column('Telefone', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'Pessoas', ['Telefone'])
    op.create_unique_constraint(None, 'Pessoas', ['RG'])
    op.create_unique_constraint(None, 'Pessoas', ['CPF'])
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
