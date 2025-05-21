{
    "name" : "vehicle management",
    "version" : "1.0",
    "depends" : ["base"],
    "author" : "Vivek Ravel",
    "category" : "custom",
    "depends" : ["base","account"],
    "description": """
        This module is for managing car details.
    """,    
    "data": [
        "data/sequence.xml",
        "security/ir.model.access.csv",
        "security/security_group.xml",
        "wizard/bill_details_wiz.xml",
        "wizard/maintenance_wiz.xml",
        "wizard/bike_maintenance_wiz.xml",
        "report/bill_report.xml",
        "views/car_details.xml",
        "views/menu.xml",
        "views/customer_details.xml",
        "views/driver_details.xml",
        # "views/bill_details.xml",
        "views/car_maintenance.xml",
        "views/bike_details.xml",
        "views/invoice_details.xml",

    ],
    "installable": True,
    "application": True,
}    
