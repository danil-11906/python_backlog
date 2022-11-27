from task_2.arbiter import Arbiter
from task_2.blockchain import BlockchainManager
from task_2.utils import generate_keys

generate_keys()

blockchain_manager = BlockchainManager()
blockchain = blockchain_manager.get_blockchain_from_arbiter()
# print(blockchain[-1])
# blockchain = blockchain_manager.get_blockchain()

# blockchain_manager.generate_blockchain()
# blockchain_manager.print_blockchain()
# blockchain_manager.check_chain_validity(blockchain)

solution_block = blockchain_manager.add_solution_block()

arbiter = blockchain_manager.get_arbiter()
arbiter.post_block(solution_block)
# arbiter.post_author()


