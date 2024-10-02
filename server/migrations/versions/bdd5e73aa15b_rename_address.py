# # """rename address

# # Revision ID: bdd5e73aa15b
# # Revises: bb0110a4f4d0
# # Create Date: 2024-10-02 17:45:26.961786

# # """
# # from alembic import op
# # import sqlalchemy as sa


# # # revision identifiers, used by Alembic.
# # revision = 'bdd5e73aa15b'
# # down_revision = 'bb0110a4f4d0'
# # branch_labels = None
# # depends_on = None


# # def upgrade():
# #     # ### commands auto generated by Alembic - please adjust! ###
# #     op.add_column('departments', sa.Column('location', sa.String(), nullable=False))
# #     op.drop_column('departments', 'address')
# #     # ### end Alembic commands ###


# # def downgrade():
# #     # ### commands auto generated by Alembic - please adjust! ###
# #     op.add_column('departments', sa.Column('address', sa.VARCHAR(), nullable=True))
# #     op.drop_column('departments', 'location')
# #     # ### end Alembic commands ###
# """rename address

# Revision ID: bdd5e73aa15b
# Revises: bb0110a4f4d0
# Create Date: 2024-10-02 17:45:26.961786

# """
# from alembic import op
# import sqlalchemy as sa

# # revision identifiers, used by Alembic.
# revision = 'bdd5e73aa15b'
# down_revision = 'bb0110a4f4d0'
# branch_labels = None
# depends_on = None


# def upgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
#     with op.batch_alter_table('departments', schema=None) as batch_op:
#         batch_op.add_column(sa.Column('location', sa.String(), nullable=False))
#         batch_op.drop_column('address')
#     # ### end Alembic commands ###


# def downgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
#     with op.batch_alter_table('departments', schema=None) as batch_op:
#         batch_op.add_column(sa.Column('address', sa.VARCHAR(), nullable=True))
#         batch_op.drop_column('location')
#     # ### end Alembic commands ###
"""rename address

Revision ID: bdd5e73aa15b
Revises: bb0110a4f4d0
Create Date: 2024-10-02 17:45:26.961786

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'bdd5e73aa15b'
down_revision = 'bb0110a4f4d0'
branch_labels = None
depends_on = None


def upgrade():
    # Rename the 'address' column to 'location' in the 'departments' table
    with op.batch_alter_table('departments', schema=None) as batch_op:
        batch_op.alter_column('address', new_column_name='location')


def downgrade():
    # Rename the 'location' column back to 'address' in the 'departments' table
    with op.batch_alter_table('departments', schema=None) as batch_op:
        batch_op.alter_column('location', new_column_name='address')
