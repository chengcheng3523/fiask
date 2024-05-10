from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from app import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from app import Flask, request, jsonify
db = SQLAlchemy()

class AccountPassword(db.Model):
    __tablename__ = 'account_password'

    ID = db.Column(db.String(255), primary_key=True)
    PASSWORD = db.Column(db.String(255), nullable=False)
    UC = db.Column(db.String(255), nullable=False)
    UN = db.Column(db.String(255), nullable=False)
    FC = db.Column(db.String(20), nullable=False)
app = Flask(__name__)

#Database connection settings
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'DevAuth'
app.config['MYSQL_PASSWORD'] = 'Dev127336'
app.config['MYSQL_DB'] = 'pydb'
mysql = MySQL(app)







def check_database_connection():
    with app.app_context():
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT 1")
            data = cur.fetchone()
            cur.close()
            print("Connected to the database successfully.")
        except Exception as e:
            print(f"Error connecting to the database: {str(e)}")

check_database_connection()



#item
@app.route('/api/items/post', methods=['POST'])
def create_items():
    data = request.get_json()
    if 'items' not in data:
        return jsonify({'error': 'Items data not provided in request'}), 400

    item = data['items']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO items (items) VALUES (%s)", (item,))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Items created'}), 201

@app.route('/api/items/get', methods=['GET'])
def get_items():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM items")
    items = cur.fetchall()
    
    # Adding 'item_id' key to each item for better identification
    items_with_id = []
    for item in items:
        if len(item) >= 2:
            items_with_id.append({'item_id': item[0], 'items': item[1]})
    
    return jsonify(items_with_id)

@app.route('/api/items/<int:item_id>/put', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    if 'items' not in data:
        return jsonify({'error': 'Item data not provided in request'}), 400
    
    new_item = data['items']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE items SET items = %s WHERE item_id = %s", (new_item, item_id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Item updated'}), 200


@app.route('/api/items/<int:item_id>/delete', methods=['DELETE'])
def delete_item(item_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM items WHERE items = %s", [item_id]) # 使用欄位名稱 'items'
    mysql.connection.commit()
    return jsonify({'status': 'Item deleted'}), 200



#item

#accountpassword
@app.route('/api/accountpassword/post', methods=['POST'])
def create_account_password():
    data = request.get_json()
    required_keys = ['ID', 'PASSWORD', 'UC', 'UN', 'FC']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `account password` (ID, PASSWORD, UC, UN, FC) VALUES (%s, %s, %s, %s, %s)", (data['ID'], data['PASSWORD'], data['UC'], data['UN'], data['FC']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'Account created'}), 201

@app.route('/api/accountpassword/get', methods=['GET'])
def get_account_password():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM `account password`")
    account_passwords = cur.fetchall()
    return jsonify(account_passwords)

@app.route('/api/accountpassword/<int:account_password_id>/put', methods=['PUT'])
def update_account_password(account_password_id):
    data = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("UPDATE `account password` SET name = %s WHERE id = %s", (data['name'], account_password_id))
    mysql.connection.commit()
    return jsonify({'status': 'Account password updated'}), 200

@app.route('/api/accountpassword/delete', methods=['DELETE'])
def delete_account_password():
    # 假設你的請求 JSON 中有帳戶ID、密碼、UC、UN 和 FC
    account_id = request.json.get('account_id')
    password = request.json.get('password')
    uc = request.json.get('uc')
    un = request.json.get('un')
    fc = request.json.get('fc')
    
    cur = mysql.connection.cursor()
    # 使用多個條件來刪除符合這些條件的記錄
    cur.execute("DELETE FROM `account password` WHERE ID = %s AND PASSWORD = %s AND UC = %s AND UN = %s AND FC = %s",
                (account_id, password, uc, un, fc))
    mysql.connection.commit()
    return jsonify({'status': 'Account password deleted'}), 200



#customer complaintsfeedback records22
@app.route('/api/customercomplaintsfeedbackrecords22/post', methods=['POST'])
def create_customercomplaintsfeedbackrecords22():
    data = request.get_json()
    required_keys = ['UC', 'Field Code', 'Date', 'CustomerName', 'CustomerPhone','Complaint','Resolution','Processor']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `customer complaintsfeedback records22` (UC, `Field Code`, Date, CustomerName, CustomerPhone, Complaint, Resolution, Processor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (data['UC'], data['Field Code'], data['Date'], data['CustomerName'], data['CustomerPhone'], data['Complaint'], data['Resolution'], data['Processor']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'Data inserted successfully'}), 201

#drying operation record18
@app.route('/api/dryingoperationrecord18/post', methods=['POST'])
def create_dryingoperationrecord18():
    data = request.get_json()
    required_keys = ['UC', 'Field Code', 'ProcessDate', 'Item', 'BatchNumber', 'FreshWeight', 'Operation', 'DryWeight', 'Remarks']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `drying operation record18` (UC, `Field Code`, ProcessDate, Item, BatchNumber, FreshWeight, Operation, DryWeight, Remarks) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['UC'], data['Field Code'], data['ProcessDate'], data['Item'], data['BatchNumber'], data['FreshWeight'], data['Operation'], data['DryWeight'], data['Remarks']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'Data inserted successfully'}), 201

#environmental materials entry exit records11
@app.route('/api/environmentalmaterialsentryexitrecords11/post', methods=['POST'])
def create_environmentalmaterialsentryexitrecords11():
    data = request.get_json()
    required_keys = ['MaterialID', 'MaterialName', 'DosageForm', 'BrandName', 'Supplier', 'PackagingUnit', 'PackagingVolume', 'Date', 'PurchaseQuantity', 'UsageQuantity', 'RemainingQuantity']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `environmental materials entry exit records11` (MaterialID, MaterialName, DosageForm, BrandName, Supplier, PackagingUnit, PackagingVolume, Date, PurchaseQuantity, UsageQuantity, RemainingQuantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['MaterialID'], data['MaterialName'], data['DosageForm'], data['BrandName'], data['Supplier'], data['PackagingUnit'], data['PackagingVolume'], data['Date'], data['PurchaseQuantity'], data['UsageQuantity'], data['RemainingQuantity']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'Data inserted successfully'}), 201

#environmentalrecords09
@app.route('/api/environmentalrecords09/post', methods=['POST'])
def create_environmentalrecords09():
    data = request.get_json()
    required_keys = ['Date Used', 'Field Code', 'Crop', 'PestTarget', 'MaterialCodeOrName', 'WaterVolume', 'ChemicalUsage', 'DilutionFactor', 'SafetyHarvestPeriod', 'OperatorMethod', 'UC']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `environmental records09` (`Date Used`, `Field Code`, `Crop`, `PestTarget`, `MaterialCodeOrName`, `WaterVolume`, `ChemicalUsage`, `DilutionFactor`, `SafetyHarvestPeriod`, `OperatorMethod`, `UC`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['Date Used'], data['Field Code'], data['Crop'], data['PestTarget'], data['MaterialCodeOrName'], data['WaterVolume'], data['ChemicalUsage'], data['DilutionFactor'], data['SafetyHarvestPeriod'], data['OperatorMethod'], data['UC']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'Data inserted successfully'}), 201


#equipmentmaintenancerecords16
@app.route('/api/equipmentmaintenancerecords16/post', methods=['POST'])
def create_equipmentmaintenancerecords16():
    data = request.get_json()
    required_keys = ['UC', 'Field Code', 'Date', 'Item', 'Operation', 'Recorder']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '请求中未提供所需数据'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `equipment maintenance records16` (`UC`, `Field Code`, `Date`, `Item`, `Operation`, `Recorder`) VALUES (%s, %s, %s, %s, %s, %s)", (data['UC'], data['Field Code'], data['Date'], data['Item'], data['Operation'], data['Recorder']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '记录已创建'}), 201

#facilitycleaningmanagementrecords15
@app.route('/api/facilitycleaningmanagementrecords15/post', methods=['POST'])
def create_facilitycleaningmanagementrecords15():
    data = request.get_json()
    required_keys = ['UC', 'Field Code', 'Date', 'Item', 'Operation', 'Recorder']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `facility cleaning management records15` (UC, `Field Code`, Date, Item, Operation, Recorder) VALUES (%s, %s, %s, %s, %s, %s)", (data['UC'], data['Field Code'], data['Date'], data['Item'], data['Operation'], data['Recorder']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'Data inserted successfully'}), 201

#fertilizerentryexitrecords08
@app.route('/api/fertilizerentryexitrecords08/post', methods=['POST'])
def create_fertilizerentryexitrecords08():
    data = request.get_json()
    required_keys = ['MaterialID', 'MaterialName', 'Manufacturer', 'Supplier', 'PackagingUnit', 'PackagingVolume', 'Date', 'PurchaseQuantity', 'UsageQuantity', 'RemainingQuantity']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `fertilizer entry exit records08` (MaterialID, MaterialName, Manufacturer, Supplier, PackagingUnit, PackagingVolume, Date, PurchaseQuantity, UsageQuantity, RemainingQuantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['MaterialID'], data['MaterialName'], data['Manufacturer'], data['Supplier'], data['PackagingUnit'], data['PackagingVolume'], data['Date'], data['PurchaseQuantity'], data['UsageQuantity'], data['RemainingQuantity']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'Data inserted successfully'}), 201

#fertilizerrecords06
@app.route('/api/fertilizerrecords06/post', methods=['POST'])
def create_fertilizerrecords06():
    data = request.get_json()
    required_keys = ['Date Used', 'Field Code', 'Crop', 'FertilizerType', 'MaterialCodeOrName', 'FertilizerAmount', 'DilutionFactor', 'Operator', 'UC']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `fertilizer records06` (`Date Used`, `Field Code`, Crop, FertilizerType, MaterialCodeOrName, FertilizerAmount, DilutionFactor, Operator, UC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['Date Used'], data['Field Code'], data['Crop'], data['FertilizerType'], data['MaterialCodeOrName'], data['FertilizerAmount'], data['DilutionFactor'], data['Operator'], data['UC']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'Data inserted successfully'}), 201

#basic data
@app.route('/api/basicdata/post', methods=['POST'])
def create_basicdata():
    data = request.get_json()
    required_keys = ['UC', 'UN', 'Farmer Name', 'Contact Phone', 'Fax', 'Mobile Phone','Address','Email','Total Cultivation Area','Number','Land Parcel Number','Area','Crop','Area Code','Area Size','Crop Type, Harvest Period, Estimated Yield', 'Notes']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '请求中未提供所需数据'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `basic data` (`UC`, `UN`, `Farmer Name`, `Contact Phone`, `Fax`, `Mobile Phone`, `Address`, `Email`, `Total Cultivation Area`, `Number`, `Land Parcel Number`, `Area`, `Crop`, `Area Code`, `Area Size`, `Crop Type, Harvest Period, Estimated Yield`, `Notes`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['UC'], data['UN'], data['Farmer Name'], data['Contact Phone'], data['Fax'], data['Mobile Phone'], data['Address'], data['Email'], data['Total Cultivation Area'], data['Number'], data['Land Parcel Number'], data['Area'], data['Crop'], data['Area Code'], data['Area Size'], data['Crop Type, Harvest Period, Estimated Yield'], data['Notes']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '记录已创建'}), 201

#harvest-post-harvest-records17
@app.route('/api/harvest-post-harvest-records17/post', methods=['POST'])
def create_harvest_post_harvest_records17():
    data = request.get_json()
    required_keys = ['HarvestDate', 'Field Code', 'CropName', 'Batch Or TraceNo', 'HarvestWeight', 'ProcessDate', 'PostHarvestTreatment', 'PostTreatmentWeight', 'VerificationStatus', 'UC']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `harvest and post-harvest handling records17` (HarvestDate, `Field Code`, CropName, `Batch Or TraceNo`, HarvestWeight, ProcessDate, PostHarvestTreatment, PostTreatmentWeight, VerificationStatus, UC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['HarvestDate'], data['Field Code'], data['CropName'], data['Batch Or TraceNo'], data['HarvestWeight'], data['ProcessDate'], data['PostHarvestTreatment'], data['PostTreatmentWeight'], data['VerificationStatus'], data['UC']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'Data inserted successfully'}), 201

#materialsandcode05071013
@app.route('/api/materialsandcode05071013/post', methods=['POST'])
def create_materialsandcode05071013():
    data = request.get_json()
    required_keys = ['UC', 'Field Code', 'NutrientMaterialCode', 'NutrientMaterialName', 'FertilizerMaterialCode', 'FertilizerMaterialName', 'PestControlMaterialCode', 'PestControlMaterialName', 'OtherMaterialCode', 'OtherMaterialName']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `materials and code05071013` (UC, `Field Code`, NutrientMaterialCode, NutrientMaterialName, FertilizerMaterialCode, FertilizerMaterialName, PestControlMaterialCode, PestControlMaterialName, OtherMaterialCode, OtherMaterialName) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['UC'], data['Field Code'], data['NutrientMaterialCode'], data['NutrientMaterialName'], data['FertilizerMaterialCode'], data['FertilizerMaterialName'], data['PestControlMaterialCode'], data['PestControlMaterialName'], data['OtherMaterialCode'], data['OtherMaterialName']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'Data inserted successfully'}), 201

#nutritional-preparation-record04
@app.route('/api/nutritional-preparation-record04/post', methods=['POST'])
def create_nutritional_preparation_record04():
    data = request.get_json()
    required_keys = ['UC', 'Field_Code', 'PreparationDate', 'MaterialCodeOrName', 'UsageAmount', 'PreparationProcess', 'FinalpHValue', 'FinalECValue', 'PreparerName']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `nutritional preparation record04` (UC, Field_Code, PreparationDate, MaterialCodeOrName, UsageAmount, PreparationProcess, FinalpHValue, FinalECValue, PreparerName) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['UC'], data['Field_Code'], data['PreparationDate'], data['MaterialCodeOrName'], data['UsageAmount'], data['PreparationProcess'], data['FinalpHValue'], data['FinalECValue'], data['PreparerName']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'Data inserted successfully'}), 201

#operator-status-check-record20
@app.route('/api/operator-status-check-record20/post', methods=['POST'])
def create_operator_status_check_record20():
    data = request.get_json()
    required_keys = ['Check item', 'Job date', 'Operator name']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `operator status check record20` (`Check item`, `Job date`, `Operator name`) VALUES (%s, %s, %s)", (data['Check item'], data['Job date'], data['Operator name']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'Data inserted successfully'}), 201

#other records12
@app.route('/api/other-records12/post', methods=['POST'])
def create_other_records12():
    data = request.get_json()
    required_keys = ['Date Used', 'Field Code', 'Crop', 'MaterialCodeOrName', 'UsageAmount', 'Operator', 'Remarks', 'UC']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `other records12` (`Date Used`, `Field Code`, Crop, MaterialCodeOrName, UsageAmount, Operator, Remarks, UC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (data['Date Used'], data['Field Code'], data['Crop'], data['MaterialCodeOrName'], data['UsageAmount'], data['Operator'], data['Remarks'], data['UC']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'Data inserted successfully'}), 201

#packaging-and-shipping-records19
@app.route('/api/packaging-and-shipping-records19/post', methods=['POST'])
def create_packaging_and_shipping_records19():
    data = request.get_json()
    required_keys = ['UC', 'Field Code', 'SaleDate', 'ProductName', 'SalesTarget', 'ShipmentQuantity', 'PackagingSpec', 'LabelUsageQuantity', 'LabelVoidQuantity', 'VerificationStatus']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `packaging and shipping records19` (UC, `Field Code`, SaleDate, ProductName, SalesTarget, ShipmentQuantity, PackagingSpec, LabelUsageQuantity, LabelVoidQuantity, VerificationStatus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['UC'], data['Field Code'], data['SaleDate'], data['ProductName'], data['SalesTarget'], data['ShipmentQuantity'], data['PackagingSpec'], data['LabelUsageQuantity'], data['LabelVoidQuantity'], data['VerificationStatus']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'Data inserted successfully'}), 201

#paste232425
@app.route('/api/paste232425/post', methods=['POST'])
def create_paste232425():
    data = request.get_json()
    required_keys = ['product', 'Product code of this batch', 'Contact date', 'Contact number', 'Shipping date', 'Export quantity', 'Labeling quantity', 'Removal date', 'Removal from shelves Quantity', 'Products removed from shelves for recycling and subsequent proce', 'Products removed from shelves for recycling and subsequent proce', 'Material purchasing documents Paste24', 'Various inspections Paste25', 'Date of receipt']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `paste232425` (product, `Product code of this batch`, `Contact date`, `Contact number`, `Shipping date`, `Export quantity`, `Labeling quantity`, `Removal date`, `Removal from shelves Quantity`, `Products removed from shelves for recycling and subsequent proce`, `Material purchasing documents Paste24`, `Various inspections Paste25`, `Date of receipt`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['product'], data['Product code of this batch'], data['Contact date'], data['Contact number'], data['Shipping date'], data['Export quantity'], data['Labeling quantity'], data['Removal date'], data['Removal from shelves Quantity'], data['Products removed from shelves for recycling and subsequent proce'], data['Material purchasing documents Paste24'], data['Various inspections Paste25'], data['Date of receipt']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'Data inserted successfully'}), 201

#records-of-entry-and-exit-of-other-materials14
@app.route('/api/records-of-entry-and-exit-of-other-materials14/post', methods=['POST'])
def create_records_of_entry_and_exit_of_other_materials14():
    data = request.get_json()
    required_keys = ['MaterialID', 'MaterialName', 'Manufacturer', 'Supplier', 'PackagingUnit', 'PackagingVolume', 'Date', 'PurchaseQuantity', 'UsageQuantity', 'RemainingQuantity']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `records of entry and exit of other materials14` (MaterialID, MaterialName, Manufacturer, Supplier, PackagingUnit, PackagingVolume, Date, PurchaseQuantity, UsageQuantity, RemainingQuantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['MaterialID'], data['MaterialName'], data['Manufacturer'], data['Supplier'], data['PackagingUnit'], data['PackagingVolume'], data['Date'], data['PurchaseQuantity'], data['UsageQuantity'], data['RemainingQuantity']))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'status': 'Data inserted successfully'}), 201

#records03
@app.route('/api/records03/post', methods=['POST'])
def create_records03():
    data = request.get_json()
    required_keys = ['UC', 'Operation Date', 'Field Code', 'Crop', 'CropContent', 'WorkItemCode']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `records03` (UC, `Operation Date`, `Field Code`, Crop, CropContent, WorkItemCode) VALUES (%s, %s, %s, %s, %s, %s)", (data['UC'], data['Operation Date'], data['Field Code'], data['Crop'], data['CropContent'], data['WorkItemCode']))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'status': 'Data inserted successfully'}), 201

#seed02
@app.route('/api/seed02/post', methods=['POST'])
def create_seed02():
    data = request.json
    required_keys = ['UC', 'UN', 'Crop', 'Cultivated Crop', 'Crop Variety', 'Seed Source', 'Seedling Purchase Date', 'Seedling Purchase Type']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Required data not provided in request'}), 400
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO seed02 (UC, UN, Crop, `Cultivated Crop`, `Crop Variety`, `Seed Source`, `Seedling Purchase Date`, `Seedling Purchase Type`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (data['UC'], data['UN'], data['Crop'], data['Cultivated Crop'], data['Crop Variety'], data['Seed Source'], data['Seedling Purchase Date'], data['Seedling Purchase Type']))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'status': 'Data inserted successfully'}), 201















@app.route('/', methods=['GET'])
def home():
    return "Welcome to my API!"
@app.errorhandler(404)
def resourcenotfound(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(KeyError)
def handlekeyerror(e):
    return jsonify(error='Key not found in request data'), 400

import uuid

unique_id = uuid.uuid4()

if __name__ == '__main__':
    # 建立資料庫表格
    with app.app_context():
        db.init_app(app)
        with app.app_context():
            db.engine.execute('''
                CREATE TABLE IF NOT EXISTS accountpassword (
                    ID INT AUTO_INCREMENT PRIMARY KEY,
                    PASSWORD VARCHAR(255) NOT NULL,
                    UC VARCHAR(255) NOT NULL,
                    UN VARCHAR(255) NOT NULL,
                    FC VARCHAR(20) NOT NULL
                )
            ''')
        app.run(debug=True)

        ##db.create_all()
        ##app.run()

    # 啟動 Flask 應用程式




# from bravado.client import SwaggerClient

# 載入Swagger API的規範文件
#swagger_spec_url = 'http://petstore.swagger.io/v2/swagger.json'

# 初始化Bravado客戶端
# client = SwaggerClient.from_url(swagger_spec_url)


# 調用API的某個方法
# response = client.pet.getPetById(petId=1).result()

# 處理響應
# if response:
#    print("響應:", response)
#else:
#   print("未找到寵物")





