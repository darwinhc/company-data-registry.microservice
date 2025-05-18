from abc import ABCMeta, abstractmethod

from bisslog import Division


class CompanyStructuredDataDivision(Division, metaclass=ABCMeta):
    """Class to handle structured data for company division."""

    @abstractmethod
    def get_company_structured_data(self, id_data: str) -> dict:
        """Retrieve structured data for a specific company.

        Parameters
        ----------
        id_data : str
            The unique identifier for the company.

        Returns
        -------
        dict
            A dictionary containing the structured data for the specified company.
        """
        ...

    @abstractmethod
    def update_company_structured_data(self, company_id: str, data: dict) -> bool:
        """Update structured data for a specific company.

        Parameters
        ----------
        company_id : str
            The unique identifier for the company.
        data : dict
            A dictionary containing the new structured data for the specified company.

        Returns
        -------
        bool
            True if the update was successful, False otherwise.
        """
        ...

    @abstractmethod
    def delete_company_structured_data(self, company_id: str) -> bool:
        """Delete structured data for a specific company.

        Parameters
        ----------
        company_id : str
            The unique identifier for the company.

        Returns
        -------
        bool
            True if the deletion was successful, False otherwise.
        """
        ...

    @abstractmethod
    def list_all_companies_structured_data(self) -> list:
        """List structured data for all companies.

        Returns
        -------
        list
            A list of dictionaries, each containing structured data for a company.
        """
        ...

    @abstractmethod
    def create_company_structured_data(self, data: dict) -> str:
        """Create structured data for a new company.

        Parameters
        ----------
        data : dict
            A dictionary containing the structured data for the new company.

        Returns
        -------
        str
            The unique identifier for the newly created company.
        """
        ...

