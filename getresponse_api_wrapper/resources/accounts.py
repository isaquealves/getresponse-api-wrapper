from typing import AnyStr, Dict, List, Optional, Union
import json
from getresponse_api_wrapper.resources import BaseResource


class Accounts(BaseResource):
    """Accounts resource
    Use this resource to access the API routes related to the
    authenticated user account.
    """

    def get_blacklists(self) -> Dict[AnyStr, List[AnyStr]]:
        """ Get account blacklist masks
        Returns
        --------
            dictionary: { "masks": ["blacklist@sample.com"]}
        """
        response = self.request.get("/accounts/blacklists")
        return response.json()

    def update_blacklists(self, data: Dict[AnyStr, List[AnyStr]] = None):
        """Update account blacklists
        Parameters
        ----------
        data: Dict
            A dictionary with "masks" key pointing to a
            list of strings (default: None)

        Returns
        -------
        dict
            a dictionary containing the same information as submitted
        """
        if not data or "masks" not in data.keys():
            raise ValueError(
                "Blacklist should be a dictionary with 'masks'"
                "key pointing to a list of blacklists"
            )

        response = self.request.post(
            "/accounts/blacklists", json=json.dumps(data)
        )
        return response.json()

    def get_account_info(self):
        response = self.request.get("/accounts")
        return response.json()
