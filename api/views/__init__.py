from .type_diagnostic import TypeDiagnosticViewSet, TypeDiagnosticFullDataViewSet
from .groups import GroupsViewSet, GroupsFullDataViewSet
from .user import UserViewSet, UserFullDataViewSet
from .advices import AdvicesViewSet, AdvicesFullDataViewSet
from .relationship import RelationshipViewSet, RelationshipFullDataViewSet
from .parents import ParentsViewSet, ParentsFullDataViewSet
from .validate_parents import ValidateParentsView
from .register_child import RegistrationChildView
from .childs import ChildsViewSet, ChildsFullDataViewSet
from .parents_childs import ParentsChildsViewSet, ParentsChildsFullDataViewSet
from .childs_detail import ChildsDetailViewSet, ChildsDetailFullDataViewSet
from .chart_child_data import ChartChildDataView
from .suggestions import SuggestionsView