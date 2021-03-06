
auth_rules = [
	{
		'is_manual_review':True,
		'role':'developer',
		'env':'prd',
		'reject':True,
		'execute':False,
		'rollback':False,
		'approve':False,
		#'disapprove':False
	},
	{
		'is_manual_review':True,
		'role':'developer_manager',
		'env':'prd',
		'reject':True,
		'execute':False,
		'rollback':False,
		'approve':True,
		#'disapprove':True
	},
	{
		'is_manual_review':True,
		'role':'developer_supremo',
		'env':'prd',
		'reject':True,
		'execute':False,
		'rollback':False,
		'approve':True,
		#'disapprove':True
	},
	{
		'is_manual_review':True,
		'role':'admin',
		'env':'prd',
		'reject':True,
		'execute':True,
		'rollback':True,
		'approve':True,
		#'disapprove':True
	},

	{
		'is_manual_review':False,
		'role':'developer',
		'env':'prd',
		'reject':True,
		'execute':False,
		'rollback':False,
		'approve':False,
		#'disapprove':False
	},
	{
		'is_manual_review':False,
		'role':'developer_manager',
		'env':'prd',
		'reject':True,
		'execute':True,
		'rollback':True,
		'approve':False,
		#'disapprove':False
	},
	{
		'is_manual_review':False,
		'role':'developer_supremo',
		'env':'prd',
		'reject':True,
		'execute':True,
		'rollback':True,
		'approve':False,
		#'disapprove':False
	},
	{
		'is_manual_review':False,
		'role':'admin',
		'env':'prd',
		'reject':True,
		'execute':True,
		'rollback':True,
		'approve':False,
		#'disapprove':False
	},

	{
		'is_manual_review':True,
		'role':'developer',
		'env':'test',
		'reject':True,
		'execute':True,
		'rollback':True,
		'approve':False,
		#'disapprove':False
	},
	{
		'is_manual_review':True,
		'role':'developer_manager',
		'env':'test',
		'reject':True,
		'execute':True,
		'rollback':True,
		'approve':False,
		#'disapprove':False
	},
	{
		'is_manual_review':True,
		'role':'developer_supremo',
		'env':'test',
		'reject':True,
		'execute':True,
		'rollback':True,
		'approve':False,
		#'disapprove':False
	},
	{
		'is_manual_review':True,
		'role':'admin',
		'env':'test',
		'reject':True,
		'execute':True,
		'rollback':True,
		'approve':False,
		#'disapprove':False
	},

	{
		'is_manual_review':False,
		'role':'developer',
		'env':'test',
		'reject':True,
		'execute':True,
		'rollback':True,
		'approve':False,
		#'disapprove':False
	},
	{
		'is_manual_review':False,
		'role':'developer_manager',
		'env':'test',
		'reject':True,
		'execute':True,
		'rollback':True,
		'approve':False,
		#'disapprove':False
	},
	{
		'is_manual_review':False,
		'role':'developer_supremo',
		'env':'test',
		'reject':True,
		'execute':True,
		'rollback':True,
		'approve':False,
		#'disapprove':False
	},
	{
		'is_manual_review':False,
		'role':'admin',
		'env':'test',
		'reject':True,
		'execute':True,
		'rollback':True,
		'approve':False,
		#'disapprove':False
	},

]
