# VNR specific fields (used in embed())
current_wsn = {}  # copy of wsn_for_this_perm represents the substrate
reduced_adj = dict()  # copy of original adjacency list of substrate
avoid = []  # holds the links that need to be penalised
has_embedding = False  # indicates if there are existing appings (used for ONLINE)
feasible = False  # controls the termination of re-tries (used for verify_feasibility)
online_flag = False   # controls embedding mode

# permutation specific fields
wsn_for_this_perm = {}  # copy of wsn represents the substrate
VWSNs = []  # feasible embeddings for each/current permutation
current_perm_emb_costs = {}  # embeddings and their costs for current permutation
overall_cost = 0  # total cost for all embeddings in each/current permutation
committed_wsn = {}  # copy of wsn_for_this_perm after identifying final/best embedding for current perm
max_accepted_vnrs = 0  # highest number of vnrs in current perm

already_mapped_vnrs = {}  # memoizes results of previous embeddings (used in independent perm blocks)
best_embeddings = {}  # best embeddings for each combination (ultimately the optimal solution) [('[8, 4, 45]', {'overall_cost': 56371.374759009785, 'permutation': 0})]


# test case specific fields
wsn = {}  # the original instance of the initialized substrate graph
active_vns = []  # copy of VWSNs, stores the list of embedded vns (used by generate_output to update mapping_dictionary)


sp_alg_str = "Dijkstra"  # identifies path finder algorithm used for test
main_sink = 0  # identifies sink node id used for test
X = 0 # used to set graph dimensions manually
Y = 0 # used to set graph dimensions manually

# Output, first three copied from input vector (used in pickle file)
nwksize = 0
numvn = 0
iteration = 0
# Following result from algorithm execution
proc_time = 0.0
#acceptance = config.max_accepted_vnr / config.numvn
mapping = dict() #: dictionary vlink:[slinks],
overall_cost = 0.0
acceptance = 0
result_vectors = [] # stores test results until written into pickle file


# performance metrics /fields
start = 0.0
perm_counter = 0
total_operations = 0
dijkstra_operations = 0
link_penalize_operations = 0
verify_operations = 0
plot_counter = 0

current_perm = []
previous_perm = []
perm_prefix = []
vns_per_perm = {} #success/fail of each vnrs per current perm
perms_list = {} #store success/fail of vnrs for all perms

prefix_length = []  # used to identify already calculated sequences to eliminate duplicate work
current_key_prefix = []

current_perm_block_results = {}
current_perm_results = {}
current_perm_block_acceptance = 0
current_perm_block_cost = 0.0
current_perm_block_best = {'acceptance':0,'overall_cost':0.0,'committed':None,'mappings':None}

current_test_best = {'acceptance':0,'overall_cost':0.0,'committed':None,'mappings':None}





