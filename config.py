import networkx as nx
from combinationIterator import CombinationIterator as ci
start = 0.0

VN_l1 = nx.DiGraph()
counter_value = 0
total_operations = 0
plot_counter = 0
avoid = []
penalized_list= []
penalize = dict()
failed_links_list = []
feasible = False
has_embedding = False


VWSNs = []  #feasible embeddings for each/current permutation
all_embeddings = [] #list of embeddings for all permutations
embedding_costs = {} #individual and overall embeddings and their cost for all permutations
current_emb_costs = {} #embeddings and their costs for current permutation
overall_cost = 0 #total cost for all embediings in each/current permutation
best_embeddings = {} #best embeddings for each combination
max_accepted_vnr = 0 #highest nuber of vnrs
vnr_list = []
allocated_links_load = dict()
allocated_links_weight = dict()
reduced_adj = dict()
link_weights = dict()
two_hops = dict()

current_wsn = nx.DiGraph()
wsn_for_this_perm = nx.DiGraph()

adjacencies_for_this_perm = dict()
link_weights_for_this_perm = dict()
wsn_for_this_perm = nx.DiGraph()

failed_sources = []
perm_indx = 0