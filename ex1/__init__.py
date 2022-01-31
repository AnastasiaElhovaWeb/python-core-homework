from mapping import RAW_MAPPING

def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    categories = []
    categoriesSrc = mapping['categories']
    rolesSrc = mapping['roles']
    categoryIdsSrc = mapping['categoryIdsSorted']

    for catId in categoryIdsSrc:
        categorySrc = categoriesSrc[catId]
        roles = []
        for roleId in categorySrc['roleIds']:
            roleSrc = rolesSrc[roleId]
            role = {
                'id': roleSrc['id'],
                'text': roleSrc['name'] 
            }
            roles.append(role)
        category = {
            'id': categorySrc['id'],
            'text': categorySrc['name'],
            'items': roles
        }
        categories.append(category)

    returnData = {
        'categories': categories
    }

    return returnData

build_roles_tree(RAW_MAPPING)