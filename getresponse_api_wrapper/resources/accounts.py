from typing import Any, AnyStr, Dict, List, Optional, Union
import json
from getresponse_api_wrapper.resources import BaseResource
from getresponse_api_wrapper import helper


class Accounts(BaseResource):
    """Accounts resource
    Use this resource to access the API routes related to the
    authenticated user account.
    """

    account_fields = [
        "countryCode",
        "industryTag",
        "firstName",
        "lastName",
        "companyName",
        "phone",
        "state",
        "city",
        "street",
        "zipCode",
        "numberOfEmployees",
        "timeFormat",
    ]

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
        """Get current user account information
        Returns
        -------
        dict
            A dictionary representing an account record
        """
        response = self.request.get("/accounts")
        return response.json()

    def update_account_info(self, data: Dict[AnyStr, Any] = None):
        """Update account information
        Parameters
        ----------
        data: Dict
            A dictionary containing one or more fields from account.
            See `Account.account_fields` for a list of account fields
        Returns
        -------
        dict
            A dictionary containing the submitted data
        Raise
        -----
        ValueError if no data is provided or data is empty
        KeyError if fields in data cannot be found in `Account.account_fields`
        """
        if not data:
            raise ValueError("Data should not be empty neither None")
        differ = helper.data_has_invalid_fields(
            self.account_fields, data.keys()
        )

        if differ:
            raise KeyError(
                f"Key(s) {', '.join([item for item in differ])}"
                "cannot be used to update account"
            )

        response = self.request.post("/accounts", json=json.dumps(data))
        return response.json()
