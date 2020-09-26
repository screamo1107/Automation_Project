**Install required packages**:

pip install -r requirements.txt

** **
**Run**:

for **Google Chrome**:
pytest -v -s -m need_review --tb=line --browser_name=chrome test_%page%.py

for **Mozilla Firefox**:
pytest -v -s -m need_review --tb=line --browser_name=firefox test_%page%.py

Example: pytest -v -s -m need_review --tb=line --browser_name=chrome test_product_page.py

** **
**Description**: 

**base_page.py** - Store all methods that apply to all Page Objects;

**%some%_page.py** - Store methods for specific Page Object + methods inherited from base_page;

**locators_m.py** - Locators stored as const;

**conftest.py** - Setup the browser itself;

**pytest.ini** - PyTest custom marks;

**requirements.txt** - Required packages to install;

**test_%some%_page.py** - Executing the tests itself by PyTest using prefix "test_";
