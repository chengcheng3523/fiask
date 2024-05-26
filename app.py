from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from app import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from app import Flask, request, jsonify
db = SQLAlchemy()
from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
ma = Marshmallow(app)


#Database connection settings
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
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

class AccountPassword(db.Model):
    __tablename__ = 'accountpassword'  # 資料表名稱修改為 'accountpassword'

    id = db.Column(db.Integer, primary_key=True)  # 主鍵欄位名稱修改為 'id'
    password = db.Column(db.String(255), nullable=False)  # 欄位名稱修改為 'password'
    uc = db.Column(db.String(255), nullable=False)  # 欄位名稱修改為 'uc'
    un = db.Column(db.String(255), nullable=False)  # 欄位名稱修改為 'un'
    fc = db.Column(db.String(20), nullable=False)  # 欄位名稱修改為 'fc'

#accountpassword
@app.route('/api/accountpassword/post', methods=['POST'])
def create_account_password():
    data = request.get_json()
    required_keys = [ 'PASSWORD', 'UC', 'UN', 'FC']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO accountpassword (PASSWORD, UC, UN, FC) VALUES (%s, %s, %s, %s)", (data['PASSWORD'], data['UC'], data['UN'], data['FC']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201


@app.route('/api/accountpassword/get', methods=['GET'])
def get_account_password():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM accountpassword")
    account_passwords = cur.fetchall()
    cur.close()
    return jsonify(account_passwords)

@app.route('/api/accountpassword/<int:id>', methods=['PUT'])
def update_account_password(id):
    data = request.get_json()

    new_password = data.get('PASSWORD')
    new_uc = data.get('UC')
    new_un = data.get('UN')
    new_fc = data.get('FC')

    if new_password is None or new_uc is None or new_un is None or new_fc is None:
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("UPDATE accountpassword SET PASSWORD = %s, UC = %s, UN = %s, FC = %s WHERE ID = %s", 
                (new_password, new_uc, new_un, new_fc, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Account password updated'}), 200

@app.route('/api/accountpassword/<int:id>', methods=['DELETE'])
def delete_account_password(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM accountpassword WHERE id = %s", [id])
    mysql.connection.commit()
    return jsonify({'status': 'Account password deleted'}), 200
#accountpassword

#basic data
@app.route('/api/basicdata/post', methods=['POST'])
def create_basicdata():
    data = request.get_json()
    required_keys = ['UN', 'FarmerName', 'ContactPhone', 'Fax', 'MobilePhone', 'Address', 'Email', 'TotalCultivationArea', 'Number', 'LandParcelNumber', 'Area', 'Crop', 'AreaCode', 'AreaSize', 'CropTypeHarvestPeriodEstimatedYield', 'Notes']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `basicdata` (`UN`, `FarmerName`, `ContactPhone`, `Fax`, `MobilePhone`, `Address`, `Email`, `TotalCultivationArea`, `Number`, `LandParcelNumber`, `Area`, `Crop`, `AreaCode`, `AreaSize`, `CropTypeHarvestPeriodEstimatedYield`, `Notes`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['UN'], data['FarmerName'], data['ContactPhone'], data['Fax'], data['MobilePhone'], data['Address'], data['Email'], data['TotalCultivationArea'], data['Number'], data['LandParcelNumber'], data['Area'], data['Crop'], data['AreaCode'], data['AreaSize'], data['CropTypeHarvestPeriodEstimatedYield'], data['Notes']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/basicdata/get', methods=['GET'])
def get_basic_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM basicdata")
    basic_data = cur.fetchall()
    cur.close()
    return jsonify(basic_data)

@app.route('/api/basicdata/<int:id>', methods=['DELETE'])
def delete_basicdata(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM basicdata WHERE id = %s", [id])
    mysql.connection.commit()
    return jsonify({'status': 'Account password deleted'}), 200

@app.route('/api/basicdata/<int:id>', methods=['PUT'])
def update_basicdata(id):
    data = request.get_json()

    new_UN = data.get('UN')
    new_FarmerName = data.get('FarmerName')
    new_ContactPhone = data.get('ContactPhone')
    new_Fax = data.get('Fax')
    new_MobilePhone = data.get('MobilePhone')
    new_Address = data.get('Address')
    new_Email = data.get('Email')
    new_TotalCultivationArea = data.get('TotalCultivationArea')
    new_Number = data.get('Number')
    new_LandParcelNumber = data.get('LandParcelNumber')
    new_Area = data.get('Area')
    new_Crop = data.get('Crop')
    new_AreaCode = data.get('AreaCode')
    new_AreaSize = data.get('AreaSize')
    new_CropTypeHarvestPeriodEstimatedYield = data.get('CropTypeHarvestPeriodEstimatedYield')
    new_Notes = data.get('Notes')

    if any(value is None for value in [new_UN, new_FarmerName, new_ContactPhone, new_Fax, new_MobilePhone, new_Address, new_Email, new_TotalCultivationArea,
                                       new_Number, new_LandParcelNumber, new_Area, new_Crop, new_AreaCode, new_AreaSize, new_CropTypeHarvestPeriodEstimatedYield, new_Notes]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE basicdata SET 
                UN = %s, 
                FarmerName = %s, 
                ContactPhone = %s, 
                Fax = %s, 
                MobilePhone = %s, 
                Address = %s, 
                Email = %s, 
                TotalCultivationArea = %s, 
                Number = %s, 
                LandParcelNumber = %s, 
                Area = %s, 
                Crop = %s, 
                AreaCode = %s, 
                AreaSize = %s, 
                CropTypeHarvestPeriodEstimatedYield = %s, 
                Notes = %s 
                WHERE ID = %s
                """, 
                (new_UN, new_FarmerName, new_ContactPhone, new_Fax, new_MobilePhone, new_Address, new_Email, new_TotalCultivationArea, 
                 new_Number, new_LandParcelNumber, new_Area, new_Crop, new_AreaCode, new_AreaSize, 
                 new_CropTypeHarvestPeriodEstimatedYield, new_Notes, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Basic data updated'}), 200
#basic data

#customer complaintsfeedback records22
@app.route('/api/customercomplaintsfeedbackrecords22/post', methods=['POST'])
def create_customercomplaintsfeedbackrecords22():
    data = request.get_json()
    required_keys = ['FieldCode', 'Date', 'CustomerName', 'CustomerPhone','Complaint','Resolution','Processor']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `customercomplaintsfeedbackrecords22` (FieldCode, Date, CustomerName, CustomerPhone, Complaint, Resolution, Processor) VALUES (%s, %s, %s, %s, %s, %s, %s)", (data['FieldCode'], data['Date'], data['CustomerName'], data['CustomerPhone'], data['Complaint'], data['Resolution'], data['Processor']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/customercomplaintsfeedbackrecords22/get', methods=['GET'])
def get_customer_complaints_feedback_records():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customercomplaintsfeedbackrecords22")
    customer_complaints_feedback_records = cur.fetchall()
    cur.close()
    return jsonify(customer_complaints_feedback_records)

@app.route('/api/customercomplaintsfeedbackrecords22/<int:id>', methods=['DELETE'])
def delete_customercomplaintsfeedbackrecords22(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM customercomplaintsfeedbackrecords22 WHERE id = %s", [id])
    mysql.connection.commit()
    return jsonify({'status': 'Account password deleted'}), 200

@app.route('/api/customercomplaintsfeedbackrecords22/<int:id>', methods=['PUT'])
def update_record(id):
    data = request.get_json()

    new_FieldCode = data.get('FieldCode')
    new_Date = data.get('Date')
    new_CustomerName = data.get('CustomerName')
    new_CustomerPhone = data.get('CustomerPhone')
    new_Complaint = data.get('Complaint')
    new_Resolution = data.get('Resolution')
    new_Processor = data.get('Processor')

    if any(value is None for value in [new_FieldCode, new_Date, new_CustomerName, new_CustomerPhone, new_Complaint, new_Resolution, new_Processor]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE customercomplaintsfeedbackrecords22 SET 
                FieldCode = %s, 
                Date = %s, 
                CustomerName = %s, 
                CustomerPhone = %s, 
                Complaint = %s, 
                Resolution = %s, 
                Processor = %s
                WHERE ID = %s
                """, 
                (new_FieldCode, new_Date, new_CustomerName, new_CustomerPhone, new_Complaint, new_Resolution, new_Processor, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#customer complaintsfeedback records22

#drying operation record18
@app.route('/api/dryingoperationrecord18/post', methods=['POST'])
def create_dryingoperationrecord18():
    data = request.get_json()
    required_keys = ['FieldCode', 'ProcessDate', 'Item', 'BatchNumber', 'FreshWeight', 'Operation', 'DryWeight', 'Remarks']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `dryingoperationrecord18` (`FieldCode`, ProcessDate, Item, BatchNumber, FreshWeight, Operation, DryWeight, Remarks) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (data['FieldCode'], data['ProcessDate'], data['Item'], data['BatchNumber'], data['FreshWeight'], data['Operation'], data['DryWeight'], data['Remarks']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/dryingoperationrecord18/get', methods=['GET'])
def get_drying_operation_record18():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dryingoperationrecord18")
    drying_operation_records = cur.fetchall()
    cur.close()
    return jsonify(drying_operation_records)

@app.route('/api/dryingoperationrecord18/<int:id>', methods=['DELETE'])
def delete_dryingoperationrecord18(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM dryingoperationrecord18 WHERE id = %s", [id])
    mysql.connection.commit()
    return jsonify({'status': 'Account password deleted'}), 200

@app.route('/api/dryingoperationrecord18/<int:id>', methods=['PUT'])
def update_dryingoperationrecord18(id):
    data = request.get_json()

    new_FieldCode = data.get('FieldCode')
    new_ProcessDate = data.get('ProcessDate')
    new_Item = data.get('Item')
    new_BatchNumber = data.get('BatchNumber')
    new_FreshWeight = data.get('FreshWeight')
    new_Operation = data.get('Operation')
    new_DryWeight = data.get('DryWeight')
    new_Remarks = data.get('Remarks')

    if any(value is None for value in [new_FieldCode, new_ProcessDate, new_Item, new_BatchNumber, new_FreshWeight, new_Operation, new_DryWeight, new_Remarks]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE dryingoperationrecord18 SET 
                FieldCode = %s, 
                ProcessDate = %s, 
                Item = %s, 
                BatchNumber = %s, 
                FreshWeight = %s, 
                Operation = %s, 
                DryWeight = %s, 
                Remarks = %s 
                WHERE ID = %s
                """, 
                (new_FieldCode, new_ProcessDate, new_Item, new_BatchNumber, new_FreshWeight, new_Operation, new_DryWeight, new_Remarks, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#drying operation record18

#environmental materials entry exit records11
@app.route('/api/environmentalmaterialsentryexitrecords11/post', methods=['POST'])
def create_environmentalmaterialsentryexitrecords11():
    data = request.get_json()
    required_keys = ['MaterialID', 'MaterialName', 'DosageForm', 'BrandName', 'Supplier', 'PackagingUnit', 'PackagingVolume', 'Date', 'PurchaseQuantity', 'UsageQuantity', 'RemainingQuantity']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `environmentalmaterialsentryexitrecords11` (MaterialID, MaterialName, DosageForm, BrandName, Supplier, PackagingUnit, PackagingVolume, Date, PurchaseQuantity, UsageQuantity, RemainingQuantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['MaterialID'], data['MaterialName'], data['DosageForm'], data['BrandName'], data['Supplier'], data['PackagingUnit'], data['PackagingVolume'], data['Date'], data['PurchaseQuantity'], data['UsageQuantity'], data['RemainingQuantity']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201


@app.route('/api/environmentalmaterialsentryexitrecords11/get', methods=['GET'])
def get_environmental_materials_entry_exit_records():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM environmentalmaterialsentryexitrecords11")
    environmental_materials_entry_exit_records = cur.fetchall()
    cur.close()
    return jsonify(environmental_materials_entry_exit_records)

@app.route('/api/environmentalmaterialsentryexitrecords11/<int:id>', methods=['DELETE'])
def delete_environmentalmaterialsentryexitrecords11(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM environmentalmaterialsentryexitrecords11 WHERE id = %s", [id])
    mysql.connection.commit()
    return jsonify({'status': 'Account password deleted'}), 200

@app.route('/api/environmentalmaterialsentryexitrecords11/<int:id>', methods=['PUT'])
def update_material_entry_exit_record(id):
    data = request.get_json()

    new_MaterialID = data.get('MaterialID')
    new_MaterialName = data.get('MaterialName')
    new_DosageForm = data.get('DosageForm')
    new_BrandName = data.get('BrandName')
    new_Supplier = data.get('Supplier')
    new_PackagingUnit = data.get('PackagingUnit')
    new_PackagingVolume = data.get('PackagingVolume')
    new_Date = data.get('Date')
    new_PurchaseQuantity = data.get('PurchaseQuantity')
    new_UsageQuantity = data.get('UsageQuantity')
    new_RemainingQuantity = data.get('RemainingQuantity')

    if any(value is None for value in [new_MaterialID, new_MaterialName, new_DosageForm, new_BrandName, new_Supplier, new_PackagingUnit, new_PackagingVolume, new_Date, new_PurchaseQuantity, new_UsageQuantity, new_RemainingQuantity]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE environmentalmaterialsentryexitrecords11 SET 
                MaterialID = %s, 
                MaterialName = %s, 
                DosageForm = %s, 
                BrandName = %s, 
                Supplier = %s, 
                PackagingUnit = %s, 
                PackagingVolume = %s, 
                Date = %s, 
                PurchaseQuantity = %s, 
                UsageQuantity = %s, 
                RemainingQuantity = %s
                WHERE ID = %s
                """, 
                (new_MaterialID, new_MaterialName, new_DosageForm, new_BrandName, new_Supplier, new_PackagingUnit, new_PackagingVolume, new_Date, new_PurchaseQuantity, new_UsageQuantity, new_RemainingQuantity, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#environmental materials entry exit records11

#environmentalrecords09
@app.route('/api/environmentalrecords09/post', methods=['POST'])
def create_environmentalrecords09():
    data = request.get_json()
    required_keys = ['DateUsed', 'FieldCode', 'Crop', 'PestTarget', 'MaterialCodeOrName', 'WaterVolume', 'ChemicalUsage', 'DilutionFactor', 'SafetyHarvestPeriod', 'OperatorMethod']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `environmentalrecords09` (`DateUsed`, `FieldCode`, `Crop`, `PestTarget`, `MaterialCodeOrName`, `WaterVolume`, `ChemicalUsage`, `DilutionFactor`, `SafetyHarvestPeriod`, `OperatorMethod`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['DateUsed'], data['FieldCode'], data['Crop'], data['PestTarget'], data['MaterialCodeOrName'], data['WaterVolume'], data['ChemicalUsage'], data['DilutionFactor'], data['SafetyHarvestPeriod'], data['OperatorMethod']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/environmentalrecords09/get', methods=['GET'])
def get_environmentalrecords09():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM environmentalrecords09")
    environmentalrecords09 = cur.fetchall()
    cur.close()
    return jsonify(environmentalrecords09)

@app.route('/api/environmentalrecords09/<int:id>', methods=['DELETE'])
def delete_environmentalrecords09(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM environmentalrecords09 WHERE id = %s", [id])
    mysql.connection.commit()
    return jsonify({'status': 'Account password deleted'}), 200

@app.route('/api/environmentalrecords09/<int:id>', methods=['PUT'])
def update_environmental_record(id):
    data = request.get_json()

    new_DateUsed = data.get('DateUsed')
    new_FieldCode = data.get('FieldCode')
    new_Crop = data.get('Crop')
    new_PestTarget = data.get('PestTarget')
    new_MaterialCodeOrName = data.get('MaterialCodeOrName')
    new_WaterVolume = data.get('WaterVolume')
    new_ChemicalUsage = data.get('ChemicalUsage')
    new_DilutionFactor = data.get('DilutionFactor')
    new_SafetyHarvestPeriod = data.get('SafetyHarvestPeriod')
    new_OperatorMethod = data.get('OperatorMethod')

    if any(value is None for value in [new_DateUsed, new_FieldCode, new_Crop, new_PestTarget, new_MaterialCodeOrName, new_WaterVolume, new_ChemicalUsage, new_DilutionFactor, new_SafetyHarvestPeriod, new_OperatorMethod]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE environmentalrecords09 SET 
                DateUsed = %s, 
                FieldCode = %s, 
                Crop = %s, 
                PestTarget = %s,
                MaterialCodeOrName = %s, 
                WaterVolume = %s, 
                ChemicalUsage = %s,
                DilutionFactor = %s, 
                SafetyHarvestPeriod = %s,
                OperatorMethod = %s
                WHERE ID = %s
                """, 
                (new_DateUsed, new_FieldCode, new_Crop, new_PestTarget, new_MaterialCodeOrName, new_WaterVolume, new_ChemicalUsage, new_DilutionFactor, new_SafetyHarvestPeriod, new_OperatorMethod, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#environmentalrecords09

#equipmentmaintenancerecords16
@app.route('/api/equipmentmaintenancerecords16/post', methods=['POST'])
def create_equipmentmaintenancerecords16():
    data = request.get_json()
    required_keys = ['FieldCode', 'Date', 'Item', 'Operation', 'Recorder']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `equipmentmaintenancerecords16` (`FieldCode`, `Date`, `Item`, `Operation`, `Recorder`) VALUES (%s, %s, %s, %s, %s)", (data['FieldCode'], data['Date'], data['Item'], data['Operation'], data['Recorder']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/equipmentmaintenancerecords16/get', methods=['GET'])
def get_equipmentmaintenancerecords16():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM equipmentmaintenancerecords16")
    equipmentmaintenancerecords16 = cur.fetchall()
    cur.close()
    return jsonify(equipmentmaintenancerecords16)

@app.route('/api/equipmentmaintenancerecords16/<int:id>', methods=['DELETE'])
def delete_equipmentmaintenancerecords16(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM equipmentmaintenancerecords16 WHERE id = %s", [id])
    mysql.connection.commit()
    return jsonify({'status': 'Account password deleted'}), 200

@app.route('/api/equipmentmaintenancerecords16/<int:id>', methods=['PUT'])
def update_maintenance_record(id):
    data = request.get_json()

    new_FieldCode = data.get('FieldCode')
    new_Date = data.get('Date')
    new_Item = data.get('Item')
    new_Operation = data.get('Operation')
    new_Recorder = data.get('Recorder')

    if any(value is None for value in [new_FieldCode, new_Date, new_Item, new_Operation, new_Recorder]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE equipmentmaintenancerecords16 SET 
                FieldCode = %s, 
                Date = %s, 
                Item = %s, 
                Operation = %s,
                Recorder = %s
                WHERE ID = %s
                """, 
                (new_FieldCode, new_Date, new_Item, new_Operation, new_Recorder, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#equipmentmaintenancerecords16

#facilitycleaningmanagementrecords15
@app.route('/api/facilitycleaningmanagementrecords15/post', methods=['POST'])
def create_facilitycleaningmanagementrecords15():
    data = request.get_json()
    required_keys = ['FieldCode', 'Date', 'Item', 'Operation', 'Recorder']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `facilitycleaningmanagementrecords15` (`FieldCode`, Date, Item, Operation, Recorder) VALUES (%s, %s, %s, %s, %s)", (data['FieldCode'], data['Date'], data['Item'], data['Operation'], data['Recorder']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/facilitycleaningmanagementrecords15/get', methods=['GET'])
def get_facilitycleaningmanagementrecords15():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM facilitycleaningmanagementrecords15")
    facilitycleaningmanagementrecords15 = cur.fetchall()
    cur.close()
    return jsonify(facilitycleaningmanagementrecords15)

@app.route('/api/facilitycleaningmanagementrecords15/<int:id>', methods=['DELETE'])
def delete_facilitycleaningmanagementrecords15(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM facilitycleaningmanagementrecords15 WHERE id = %s", [id])
    mysql.connection.commit()
    return jsonify({'status': 'Account password deleted'}), 200

@app.route('/api/facilitycleaningmanagementrecords15/<int:id>', methods=['PUT'])
def update_facility_cleaning_record(id):
    data = request.get_json()

    new_FieldCode = data.get('FieldCode')
    new_Date = data.get('Date')
    new_Item = data.get('Item')
    new_Operation = data.get('Operation')
    new_Recorder = data.get('Recorder')

    if any(value is None for value in [new_FieldCode, new_Date, new_Item, new_Operation, new_Recorder]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE facilitycleaningmanagementrecords15 SET 
                FieldCode = %s, 
                Date = %s, 
                Item = %s, 
                Operation = %s, 
                Recorder = %s
                WHERE ID = %s
                """, 
                (new_FieldCode, new_Date, new_Item, new_Operation, new_Recorder, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#facilitycleaningmanagementrecords15

#fertilizerentryexitrecords08
@app.route('/api/fertilizerentryexitrecords08/post', methods=['POST'])
def create_fertilizerentryexitrecords08():
    data = request.get_json()
    required_keys = ['MaterialID', 'MaterialName', 'Manufacturer', 'Supplier', 'PackagingUnit', 'PackagingVolume', 'Date', 'PurchaseQuantity', 'UsageQuantity', 'RemainingQuantity']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `fertilizerentryexitrecords08` (MaterialID, MaterialName, Manufacturer, Supplier, PackagingUnit, PackagingVolume, Date, PurchaseQuantity, UsageQuantity, RemainingQuantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['MaterialID'], data['MaterialName'], data['Manufacturer'], data['Supplier'], data['PackagingUnit'], data['PackagingVolume'], data['Date'], data['PurchaseQuantity'], data['UsageQuantity'], data['RemainingQuantity']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/fertilizerentryexitrecords08/get', methods=['GET'])
def get_fertilizerentryexitrecords08():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM fertilizerentryexitrecords08")
    fertilizerentryexitrecords08 = cur.fetchall()
    cur.close()
    return jsonify(fertilizerentryexitrecords08)

@app.route('/api/fertilizerentryexitrecords08/<int:id>', methods=['DELETE'])
def delete_fertilizerentryexitrecords08(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM fertilizerentryexitrecords08 WHERE id = %s", [id])
    mysql.connection.commit()
    return jsonify({'status': 'Account password deleted'}), 200

@app.route('/api/fertilizerentryexitrecords08/<int:id>', methods=['PUT'])
def update_fertilizer_record(id):
    data = request.get_json()

    new_MaterialID = data.get('MaterialID')
    new_MaterialName = data.get('MaterialName')
    new_Manufacturer = data.get('Manufacturer')
    new_Supplier = data.get('Supplier')
    new_PackagingUnit = data.get('PackagingUnit')
    new_PackagingVolume = data.get('PackagingVolume')
    new_Date = data.get('Date')
    new_PurchaseQuantity = data.get('PurchaseQuantity')
    new_UsageQuantity = data.get('UsageQuantity')
    new_RemainingQuantity = data.get('RemainingQuantity')

    if any(value is None for value in [new_MaterialID, new_MaterialName, new_Manufacturer, new_Supplier, new_PackagingUnit, new_PackagingVolume, new_Date, new_PurchaseQuantity, new_UsageQuantity, new_RemainingQuantity]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE fertilizerentryexitrecords08 SET 
                MaterialID = %s, 
                MaterialName = %s, 
                Manufacturer = %s,
                Supplier = %s, 
                PackagingUnit = %s, 
                PackagingVolume = %s,
                Date = %s, 
                PurchaseQuantity = %s,
                UsageQuantity = %s,
                RemainingQuantity = %s
                WHERE ID = %s
                """, 
                (new_MaterialID, new_MaterialName, new_Manufacturer, new_Supplier, new_PackagingUnit, new_PackagingVolume, new_Date, new_PurchaseQuantity, new_UsageQuantity, new_RemainingQuantity, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#fertilizerentryexitrecords08

#fertilizerrecords06
@app.route('/api/fertilizerrecords06/post', methods=['POST'])
def create_fertilizerrecords06():
    data = request.get_json()
    required_keys = ['DateUsed', 'FieldCode', 'Crop', 'FertilizerType', 'MaterialCodeOrName', 'FertilizerAmount', 'DilutionFactor', 'Operator']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `fertilizerrecords06` (`DateUsed`, `FieldCode`, Crop, FertilizerType, MaterialCodeOrName, FertilizerAmount, DilutionFactor, Operator) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (data['DateUsed'], data['FieldCode'], data['Crop'], data['FertilizerType'], data['MaterialCodeOrName'], data['FertilizerAmount'], data['DilutionFactor'], data['Operator']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/fertilizerrecords06/get', methods=['GET'])
def get_fertilizerrecords06():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM fertilizerrecords06")
    fertilizerrecords06 = cur.fetchall()
    cur.close()
    return jsonify(fertilizerrecords06)

@app.route('/api/fertilizerrecords06/<int:id>', methods=['DELETE'])
def delete_fertilizerrecords06(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM fertilizerrecords06 WHERE id = %s", [id])
    mysql.connection.commit()
    return jsonify({'status': 'Account password deleted'}), 200

@app.route('/api/fertilizerrecords06/<int:id>', methods=['PUT'])
def update_fertilizer_records(id):
    data = request.get_json()

    new_DateUsed = data.get('DateUsed')
    new_FieldCode = data.get('FieldCode')
    new_Crop = data.get('Crop')
    new_FertilizerType = data.get('FertilizerType')
    new_MaterialCodeOrName = data.get('MaterialCodeOrName')
    new_FertilizerAmount = data.get('FertilizerAmount')
    new_DilutionFactor = data.get('DilutionFactor')
    new_Operator = data.get('Operator')

    if any(value is None for value in [new_DateUsed, new_FieldCode, new_Crop, new_FertilizerType, new_MaterialCodeOrName, new_FertilizerAmount, new_DilutionFactor, new_Operator]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE fertilizerrecords06 SET 
                DateUsed = %s, 
                FieldCode = %s, 
                Crop = %s, 
                FertilizerType = %s, 
                MaterialCodeOrName = %s,
                FertilizerAmount = %s, 
                DilutionFactor = %s,
                Operator = %s
                WHERE ID = %s
                """, 
                (new_DateUsed, new_FieldCode, new_Crop, new_FertilizerType, new_MaterialCodeOrName, new_FertilizerAmount, new_DilutionFactor, new_Operator, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#fertilizerrecords06

#harvestandpostharvesthandlingrecords17
@app.route('/api/harvestandpostharvesthandlingrecords17/post', methods=['POST'])
def create_harvestandpostharvesthandlingrecords17():
    data = request.get_json()
    required_keys = ['HarvestDate', 'FieldCode', 'CropName', 'BatchOrTraceNo', 'HarvestWeight', 'ProcessDate', 'PostHarvestTreatment', 'PostTreatmentWeight', 'VerificationStatus']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `harvestandpostharvesthandlingrecords17` (`HarvestDate`, `FieldCode`, `CropName`, `BatchOrTraceNo`, `HarvestWeight`, `ProcessDate`, `PostHarvestTreatment`, `PostTreatmentWeight`, `VerificationStatus`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['HarvestDate'], data['FieldCode'], data['CropName'], data['BatchOrTraceNo'], data['HarvestWeight'], data['ProcessDate'], data['PostHarvestTreatment'], data['PostTreatmentWeight'], data['VerificationStatus']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/harvestandpostharvesthandlingrecords17/get', methods=['GET'])
def get_harvestandpostharvesthandlingrecords17():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM harvestandpostharvesthandlingrecords17")
    harvestandpostharvesthandlingrecords17 = cur.fetchall()
    cur.close()
    return jsonify(harvestandpostharvesthandlingrecords17)

@app.route('/api/harvestandpostharvesthandlingrecords17/<int:id>', methods=['DELETE'])
def delete_harvestandpostharvesthandlingrecords17(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM harvestandpostharvesthandlingrecords17 WHERE id = %s", [id])
    mysql.connection.commit()
    return jsonify({'status': 'Account password deleted'}), 200

@app.route('/api/harvestandpostharvesthandlingrecords17/<int:id>', methods=['PUT'])
def update_harvest_handling_record(id):
    data = request.get_json()

    new_HarvestDate = data.get('HarvestDate')
    new_FieldCode = data.get('FieldCode')
    new_CropName = data.get('CropName')
    new_BatchOrTraceNo = data.get('BatchOrTraceNo')
    new_HarvestWeight = data.get('HarvestWeight')
    new_ProcessDate = data.get('ProcessDate')
    new_PostHarvestTreatment = data.get('PostHarvestTreatment')
    new_PostTreatmentWeight = data.get('PostTreatmentWeight')
    new_VerificationStatus = data.get('VerificationStatus')

    if any(value is None for value in [new_HarvestDate, new_FieldCode, new_CropName, new_BatchOrTraceNo, new_HarvestWeight, new_ProcessDate, new_PostHarvestTreatment, new_PostTreatmentWeight, new_VerificationStatus]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE harvestandpostharvesthandlingrecords17 SET 
                HarvestDate = %s, 
                FieldCode = %s, 
                CropName = %s, 
                BatchOrTraceNo = %s, 
                HarvestWeight = %s,
                ProcessDate = %s, 
                PostHarvestTreatment = %s,
                PostTreatmentWeight = %s, 
                VerificationStatus = %s
                WHERE ID = %s
                """, 
                (new_HarvestDate, new_FieldCode, new_CropName, new_BatchOrTraceNo, new_HarvestWeight, new_ProcessDate, new_PostHarvestTreatment, new_PostTreatmentWeight, new_VerificationStatus, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#harvestandpostharvesthandlingrecords17

#item
@app.route('/api/items/post', methods=['POST'])
def create_items():
    data = request.get_json()
    if 'items' not in data:
        return jsonify({'error': '資料輸入失敗'}), 400

    item = data['items']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO items (items) VALUES (%s)", (item,))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/items/get', methods=['GET'])
def get_items():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM items")
    items = cur.fetchall()
    cur.close()
    return jsonify(items)

@app.route('/api/items/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.get_json()
    if 'items' not in data:
        return jsonify({'error': 'Item data not provided in request'}), 400
    
    new_item = data['items']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE items SET items = %s WHERE ID = %s", (new_item, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Item updated'}), 200

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM items WHERE id = %s", [item_id]) 
    mysql.connection.commit()
    return jsonify({'status': 'Item deleted'}), 200

#item

#materialsandcode05071013
@app.route('/api/materialsandcode05071013/post', methods=['POST'])
def create_materialsandcode05071013():
    data = request.get_json()
    required_keys = ['FieldCode', 'NutrientMaterialCode', 'NutrientMaterialName', 'FertilizerMaterialCode', 'FertilizerMaterialName', 'PestControlMaterialCode', 'PestControlMaterialName', 'OtherMaterialCode', 'OtherMaterialName']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `materialsandcode05071013` (`FieldCode`, NutrientMaterialCode, NutrientMaterialName, FertilizerMaterialCode, FertilizerMaterialName, PestControlMaterialCode, PestControlMaterialName, OtherMaterialCode, OtherMaterialName) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['FieldCode'], data['NutrientMaterialCode'], data['NutrientMaterialName'], data['FertilizerMaterialCode'], data['FertilizerMaterialName'], data['PestControlMaterialCode'], data['PestControlMaterialName'], data['OtherMaterialCode'], data['OtherMaterialName']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/materialsandcode05071013/get', methods=['GET'])
def get_materialsandcode05071013():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM materialsandcode05071013")
    materialsandcode05071013 = cur.fetchall()
    cur.close()
    return jsonify(materialsandcode05071013)

@app.route('/api/materialsandcode05071013/<int:item_id>', methods=['DELETE'])
def delete_materialsandcode05071013(item_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM materialsandcode05071013 WHERE id = %s", [item_id]) 
    mysql.connection.commit()
    return jsonify({'status': 'Item deleted'}), 200

@app.route('/api/materialsandcode05071013/<int:id>', methods=['PUT'])
def update_materials_code_record(id):
    data = request.get_json()

    new_FieldCode = data.get('FieldCode')
    new_NutrientMaterialCode = data.get('NutrientMaterialCode')
    new_NutrientMaterialName = data.get('NutrientMaterialName')
    new_FertilizerMaterialCode = data.get('FertilizerMaterialCode')
    new_FertilizerMaterialName = data.get('FertilizerMaterialName')
    new_PestControlMaterialCode = data.get('PestControlMaterialCode')
    new_PestControlMaterialName = data.get('PestControlMaterialName')
    new_OtherMaterialCode = data.get('OtherMaterialCode')
    new_OtherMaterialName = data.get('OtherMaterialName')

    if any(value is None for value in [new_FieldCode, new_NutrientMaterialCode, new_NutrientMaterialName, new_FertilizerMaterialCode, new_FertilizerMaterialName, new_PestControlMaterialCode, new_PestControlMaterialName, new_OtherMaterialCode, new_OtherMaterialName]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE materialsandcode05071013 SET 
                FieldCode = %s, 
                NutrientMaterialCode = %s, 
                NutrientMaterialName = %s, 
                FertilizerMaterialCode = %s, 
                FertilizerMaterialName = %s,
                PestControlMaterialCode = %s, 
                PestControlMaterialName = %s,
                OtherMaterialCode = %s, 
                OtherMaterialName = %s
                WHERE ID = %s
                """, 
                (new_FieldCode, new_NutrientMaterialCode, new_NutrientMaterialName, new_FertilizerMaterialCode, new_FertilizerMaterialName, new_PestControlMaterialCode, new_PestControlMaterialName, new_OtherMaterialCode, new_OtherMaterialName, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#materialsandcode05071013

#nutritionalpreparationrecord04
@app.route('/api/nutritionalpreparationrecord04/post', methods=['POST'])
def create_nutritionalpreparationrecord04():
    data = request.get_json()
    required_keys = ['FieldCode', 'PreparationDate', 'MaterialCodeOrName', 'UsageAmount', 'PreparationProcess', 'FinalpHValue', 'FinalECValue', 'PreparerName']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `nutritionalpreparationrecord04` (FieldCode, PreparationDate, MaterialCodeOrName, UsageAmount, PreparationProcess, FinalpHValue, FinalECValue, PreparerName) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (data['FieldCode'], data['PreparationDate'], data['MaterialCodeOrName'], data['UsageAmount'], data['PreparationProcess'], data['FinalpHValue'], data['FinalECValue'], data['PreparerName']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/nutritionalpreparationrecord04/get', methods=['GET'])
def get_nutritionalpreparationrecord04():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM nutritionalpreparationrecord04")
    nutritionalpreparationrecord04 = cur.fetchall()
    cur.close()
    return jsonify(nutritionalpreparationrecord04)

@app.route('/api/nutritionalpreparationrecord04/<int:item_id>', methods=['DELETE'])
def delete_nutritionalpreparationrecord04(item_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM nutritionalpreparationrecord04 WHERE id = %s", [item_id]) 
    mysql.connection.commit()
    return jsonify({'status': 'Item deleted'}), 200

@app.route('/api/nutritionalpreparationrecord04/<int:id>', methods=['PUT'])
def update_nutritional_prep_record(id):
    data = request.get_json()

    new_FieldCode = data.get('FieldCode')
    new_PreparationDate = data.get('PreparationDate')
    new_MaterialCodeOrName = data.get('MaterialCodeOrName')
    new_UsageAmount = data.get('UsageAmount')
    new_PreparationProcess = data.get('PreparationProcess')
    new_FinalpHValue = data.get('FinalpHValue')
    new_FinalECValue = data.get('FinalECValue')
    new_PreparerName = data.get('PreparerName')

    if any(value is None for value in [new_FieldCode, new_PreparationDate, new_MaterialCodeOrName, new_UsageAmount, new_PreparationProcess, new_FinalpHValue, new_FinalECValue, new_PreparerName]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE nutritionalpreparationrecord04 SET 
                FieldCode = %s, 
                PreparationDate = %s, 
                MaterialCodeOrName = %s,
                UsageAmount = %s, 
                PreparationProcess = %s, 
                FinalpHValue = %s, 
                FinalECValue = %s, 
                PreparerName = %s
                WHERE ID = %s
                """, 
                (new_FieldCode, new_PreparationDate, new_MaterialCodeOrName, new_UsageAmount, new_PreparationProcess, new_FinalpHValue, new_FinalECValue, new_PreparerName, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#nutritionalpreparationrecord04

#operatorstatuscheckrecord20
@app.route('/api/operatorstatuscheckrecord20/post', methods=['POST'])
def create_operatorstatuscheckrecord20():
    data = request.get_json()
    required_keys = ['Checkitem', 'Jobdate', 'Operatorname']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `operatorstatuscheckrecord20` (`Checkitem`, `Jobdate`, `Operatorname`) VALUES (%s, %s, %s)", (data['Checkitem'], data['Jobdate'], data['Operatorname']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/operatorstatuscheckrecord20/get', methods=['GET'])
def get_operatorstatuscheckrecord20():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM operatorstatuscheckrecord20")
    operatorstatuscheckrecord20 = cur.fetchall()
    cur.close()
    return jsonify(operatorstatuscheckrecord20)

@app.route('/api/operatorstatuscheckrecord20/<int:item_id>', methods=['DELETE'])
def delete_operatorstatuscheckrecord20(item_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM operatorstatuscheckrecord20 WHERE id = %s", [item_id]) 
    mysql.connection.commit()
    return jsonify({'status': 'Item deleted'}), 200

@app.route('/api/operatorstatuscheckrecord20/<int:id>', methods=['PUT'])
def update_operator_status_record(id):
    data = request.get_json()

    new_Checkitem = data.get('Checkitem')
    new_Jobdate = data.get('Jobdate')
    new_Operatorname = data.get('Operatorname')

    if any(value is None for value in [new_Checkitem, new_Jobdate, new_Operatorname]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE operatorstatuscheckrecord20 SET 
                Checkitem = %s, 
                Jobdate = %s, 
                Operatorname = %s
                WHERE ID = %s
                """, 
                (new_Checkitem, new_Jobdate, new_Operatorname, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Operator status record updated'}), 200

#operatorstatuscheckrecord20

#other records12
@app.route('/api/otherrecords12/post', methods=['POST'])
def create_otherrecords12():
    data = request.get_json()
    required_keys = ['DateUsed', 'FieldCode', 'Crop', 'MaterialCodeOrName', 'UsageAmount', 'Operator', 'Remarks']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `otherrecords12` (`DateUsed`, `FieldCode`, Crop, MaterialCodeOrName, UsageAmount, Operator, Remarks) VALUES (%s, %s, %s, %s, %s, %s, %s)", (data['DateUsed'], data['FieldCode'], data['Crop'], data['MaterialCodeOrName'], data['UsageAmount'], data['Operator'], data['Remarks']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201
@app.route('/api/otherrecords12/get', methods=['GET'])
def get_otherrecords12():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM otherrecords12")
    otherrecords12 = cur.fetchall()
    cur.close()
    return jsonify(otherrecords12)

@app.route('/api/otherrecords12/<int:item_id>', methods=['DELETE'])
def delete_otherrecords12(item_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM otherrecords12 WHERE id = %s", [item_id]) 
    mysql.connection.commit()
    return jsonify({'status': 'Item deleted'}), 200

@app.route('/api/otherrecords12/<int:id>', methods=['PUT'])
def update_other_records(id):
    data = request.get_json()

    new_DateUsed = data.get('DateUsed')
    new_FieldCode = data.get('FieldCode')
    new_Crop = data.get('Crop')
    new_MaterialCodeOrName = data.get('MaterialCodeOrName')
    new_UsageAmount = data.get('UsageAmount')
    new_Operator = data.get('Operator')
    new_Remarks = data.get('Remarks')

    if any(value is None for value in [new_DateUsed, new_FieldCode, new_Crop, new_MaterialCodeOrName, new_UsageAmount, new_Operator, new_Remarks]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE otherrecords12 SET 
                DateUsed = %s, 
                FieldCode = %s, 
                Crop = %s,
                MaterialCodeOrName = %s, 
                UsageAmount = %s, 
                Operator = %s,
                Remarks = %s
                WHERE ID = %s
                """, 
                (new_DateUsed, new_FieldCode, new_Crop, new_MaterialCodeOrName, new_UsageAmount, new_Operator, new_Remarks, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#other records12

#packagingandshippingrecords19

@app.route('/api/packagingandshippingrecords19/post', methods=['POST'])
def create_packagingandshippingrecords19():
    data = request.get_json()
    required_keys = ['FieldCode', 'SaleDate', 'ProductName', 'SalesTarget', 'ShipmentQuantity', 'PackagingSpec', 'LabelUsageQuantity', 'LabelVoidQuantity', 'VerificationStatus']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `packagingandshippingrecords19` (`FieldCode`, SaleDate, ProductName, SalesTarget, ShipmentQuantity, PackagingSpec, LabelUsageQuantity, LabelVoidQuantity, VerificationStatus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['FieldCode'], data['SaleDate'], data['ProductName'], data['SalesTarget'], data['ShipmentQuantity'], data['PackagingSpec'], data['LabelUsageQuantity'], data['LabelVoidQuantity'], data['VerificationStatus']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/packagingandshippingrecords19/get', methods=['GET'])
def get_packagingandshippingrecords19():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM packagingandshippingrecords19")
    packagingandshippingrecords19 = cur.fetchall()
    cur.close()
    return jsonify(packagingandshippingrecords19)

@app.route('/api/packagingandshippingrecords19/<int:item_id>', methods=['DELETE'])
def delete_packagingandshippingrecords19(item_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM packagingandshippingrecords19 WHERE id = %s", [item_id]) 
    mysql.connection.commit()
    return jsonify({'status': 'Item deleted'}), 200

@app.route('/api/packagingandshippingrecords19/<int:id>', methods=['PUT'])
def update_packaging_shipping_record(id):
    data = request.get_json()

    new_FieldCode = data.get('FieldCode')
    new_SaleDate = data.get('SaleDate')
    new_ProductName = data.get('ProductName')
    new_SalesTarget = data.get('SalesTarget')
    new_ShipmentQuantity = data.get('ShipmentQuantity')
    new_PackagingSpec = data.get('PackagingSpec')
    new_LabelUsageQuantity = data.get('LabelUsageQuantity')
    new_LabelVoidQuantity = data.get('LabelVoidQuantity')
    new_VerificationStatus = data.get('VerificationStatus')

    if any(value is None for value in [new_FieldCode, new_SaleDate, new_ProductName, new_SalesTarget, new_ShipmentQuantity, new_PackagingSpec, new_LabelUsageQuantity, new_LabelVoidQuantity, new_VerificationStatus]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE packagingandshippingrecords19 SET 
                FieldCode = %s, 
                SaleDate = %s, 
                ProductName = %s, 
                SalesTarget = %s, 
                ShipmentQuantity = %s,
                PackagingSpec = %s, 
                LabelUsageQuantity = %s,
                LabelVoidQuantity = %s, 
                VerificationStatus = %s
                WHERE ID = %s
                """, 
                (new_FieldCode, new_SaleDate, new_ProductName, new_SalesTarget, new_ShipmentQuantity, new_PackagingSpec, new_LabelUsageQuantity, new_LabelVoidQuantity, new_VerificationStatus, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#packagingandshippingrecords19

#paste232425
@app.route('/api/paste232425/post', methods=['POST'])
def create_paste232425():
    data = request.get_json()
    required_keys = ['product', 'Productcodeofthisbatch', 'Contactdate', 'Contactnumber', 'Shippingdate', 'Exportquantity', 'Labelingquantity', 'Removaldate', 'RemovalfromshelvesQuantity', 'Productsremovedfromshelvesforrecyclingandsubsequentproce', 'Productsremovedfromshelvesforrecyclingandsubsequentproce', 'MaterialpurchasingdocumentsPaste24', 'VariousinspectionsPaste25', 'Dateofreceipt']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `paste232425` (product, `Productcodeofthisbatch`, `Contactdate`, `Contactnumber`, `Shippingdate`, `Exportquantity`, `Labelingquantity`, `Removaldate`, `RemovalfromshelvesQuantity`, `Productsremovedfromshelvesforrecyclingandsubsequentproce`, `MaterialpurchasingdocumentsPaste24`, `VariousinspectionsPaste25`, `Dateofreceipt`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['product'], data['Productcodeofthisbatch'], data['Contactdate'], data['Contactnumber'], data['Shippingdate'], data['Exportquantity'], data['Labelingquantity'], data['Removaldate'], data['RemovalfromshelvesQuantity'], data['Productsremovedfromshelvesforrecyclingandsubsequentproce'], data['MaterialpurchasingdocumentsPaste24'], data['VariousinspectionsPaste25'], data['Dateofreceipt']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/paste232425/get', methods=['GET'])
def get_paste232425():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM paste232425")
    paste232425 = cur.fetchall()
    cur.close()
    return jsonify(paste232425)

@app.route('/api/paste232425/<int:item_id>', methods=['DELETE'])
def delete_paste232425(item_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM paste232425 WHERE id = %s", [item_id]) 
    mysql.connection.commit()
    return jsonify({'status': 'Item deleted'}), 200

@app.route('/api/paste232425/<int:id>', methods=['PUT'])
def update_paste_record(id):
    data = request.get_json()

    new_product = data.get('product')
    new_Productcodeofthisbatch = data.get('Productcodeofthisbatch')
    new_Contactdate = data.get('Contactdate')
    new_Contactnumber = data.get('Contactnumber')
    new_Shippingdate = data.get('Shippingdate')
    new_Exportquantity = data.get('Exportquantity')
    new_Labelingquantity = data.get('Labelingquantity')
    new_Removaldate = data.get('Removaldate')
    new_RemovalfromshelvesQuantity = data.get('RemovalfromshelvesQuantity')
    new_Productsremovedfromshelvesforrecyclingandsubsequentproce = data.get('Productsremovedfromshelvesforrecyclingandsubsequentproce')
    new_MaterialpurchasingdocumentsPaste24 = data.get('MaterialpurchasingdocumentsPaste24')
    new_VariousinspectionsPaste25 = data.get('VariousinspectionsPaste25')
    new_Dateofreceipt = data.get('Dateofreceipt')

    if any(value is None for value in [
        new_product, 
        new_Productcodeofthisbatch, 
        new_Contactdate, 
        new_Contactnumber, 
        new_Shippingdate, 
        new_Exportquantity, 
        new_Labelingquantity, 
        new_Removaldate, 
        new_RemovalfromshelvesQuantity, 
        new_Productsremovedfromshelvesforrecyclingandsubsequentproce, 
        new_MaterialpurchasingdocumentsPaste24, 
        new_VariousinspectionsPaste25, 
        new_Dateofreceipt
    ]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE paste232425 SET 
                product = %s, 
                Productcodeofthisbatch = %s, 
                Contactdate = %s, 
                Contactnumber = %s, 
                Shippingdate = %s,
                Exportquantity = %s, 
                Labelingquantity = %s,
                Removaldate = %s, 
                RemovalfromshelvesQuantity = %s,
                Productsremovedfromshelvesforrecyclingandsubsequentproce = %s, 
                MaterialpurchasingdocumentsPaste24 = %s,
                                VariousinspectionsPaste25 = %s, 
                Dateofreceipt = %s
                WHERE ID = %s
                """, 
                (new_product, 
                new_Productcodeofthisbatch, 
                new_Contactdate, 
                new_Contactnumber, 
                new_Shippingdate, 
                new_Exportquantity, 
                new_Labelingquantity, 
                new_Removaldate, 
                new_RemovalfromshelvesQuantity, 
                new_Productsremovedfromshelvesforrecyclingandsubsequentproce, 
                new_MaterialpurchasingdocumentsPaste24, 
                new_VariousinspectionsPaste25,
                new_Dateofreceipt,
                id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#paste232425

#records03
@app.route('/api/records03/post', methods=['POST'])
def create_records03():
    data = request.get_json()
    required_keys = ['OperationDate', 'FieldCode', 'Crop', 'CropContent', 'WorkItemCode']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `records03` ( `OperationDate`, `FieldCode`, Crop, CropContent, WorkItemCode) VALUES (%s, %s, %s, %s, %s)", (data['OperationDate'], data['FieldCode'], data['Crop'], data['CropContent'], data['WorkItemCode']))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/records03/get', methods=['GET'])
def get_records03():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM records03")
    records03 = cur.fetchall()
    cur.close()
    return jsonify(records03)

@app.route('/api/records03/<int:item_id>', methods=['DELETE'])
def delete_records03(item_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM records03 WHERE id = %s", [item_id]) 
    mysql.connection.commit()
    return jsonify({'status': 'Item deleted'}), 200

@app.route('/api/records03/<int:id>', methods=['PUT'])
def update_records03(id):
    data = request.get_json()

    new_OperationDate = data.get('OperationDate')
    new_FieldCode = data.get('FieldCode')
    new_Crop = data.get('Crop')
    new_CropContent = data.get('CropContent')
    new_WorkItemCode = data.get('WorkItemCode')

    if any(value is None for value in [new_OperationDate, new_FieldCode, new_Crop, new_CropContent, new_WorkItemCode]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE records03 SET 
                OperationDate = %s, 
                FieldCode = %s, 
                Crop = %s, 
                CropContent = %s, 
                WorkItemCode = %s
                WHERE ID = %s
                """, 
                (new_OperationDate, new_FieldCode, new_Crop, new_CropContent, new_WorkItemCode, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#records03

#recordsofentryandexitofothermaterials14
@app.route('/api/recordsofentryandexitofothermaterials14/post', methods=['POST'])
def create_recordsofentryandexitofothermaterials14():
    data = request.get_json()
    required_keys = ['MaterialID', 'MaterialName', 'Manufacturer', 'Supplier', 'PackagingUnit', 'PackagingVolume', 'Date', 'PurchaseQuantity', 'UsageQuantity', 'RemainingQuantity']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `recordsofentryandexitofothermaterials14` (MaterialID, MaterialName, Manufacturer, Supplier, PackagingUnit, PackagingVolume, Date, PurchaseQuantity, UsageQuantity, RemainingQuantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['MaterialID'], data['MaterialName'], data['Manufacturer'], data['Supplier'], data['PackagingUnit'], data['PackagingVolume'], data['Date'], data['PurchaseQuantity'], data['UsageQuantity'], data['RemainingQuantity']))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/recordsofentryandexitofothermaterials14/get', methods=['GET'])

@app.route('/api/recordsofentryandexitofothermaterials14/<int:item_id>', methods=['DELETE'])
def delete_recordsofentryandexitofothermaterials14(item_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM recordsofentryandexitofothermaterials14 WHERE id = %s", [item_id]) 
    mysql.connection.commit()
    return jsonify({'status': 'Item deleted'}), 200

@app.route('/api/recordsofentryandexitofothermaterials14/<int:id>', methods=['PUT'])
def update_materials_record(id):
    data = request.get_json()

    new_MaterialID = data.get('MaterialID')
    new_MaterialName = data.get('MaterialName')
    new_Manufacturer = data.get('Manufacturer')
    new_Supplier = data.get('Supplier')
    new_PackagingUnit = data.get('PackagingUnit')
    new_PackagingVolume = data.get('PackagingVolume')
    new_Date = data.get('Date')
    new_PurchaseQuantity = data.get('PurchaseQuantity')
    new_UsageQuantity = data.get('UsageQuantity')
    new_RemainingQuantity = data.get('RemainingQuantity')

    if any(value is None for value in [
        new_MaterialID, 
        new_MaterialName, 
        new_Manufacturer, 
        new_Supplier, 
        new_PackagingUnit, 
        new_PackagingVolume, 
        new_Date, 
        new_PurchaseQuantity, 
        new_UsageQuantity, 
        new_RemainingQuantity
    ]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE recordsofentryandexitofothermaterials14 SET 
                MaterialID = %s, 
                MaterialName = %s, 
                Manufacturer = %s, 
                Supplier = %s, 
                PackagingUnit = %s, 
                PackagingVolume = %s,
                Date = %s, 
                PurchaseQuantity = %s,
                UsageQuantity = %s, 
                RemainingQuantity = %s
                WHERE ID = %s
                """, 
                (new_MaterialID, new_MaterialName, new_Manufacturer, new_Supplier, new_PackagingUnit, new_PackagingVolume, new_Date, new_PurchaseQuantity, new_UsageQuantity, new_RemainingQuantity, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Record updated'}), 200

#recordsofentryandexitofothermaterials14

#seed02
@app.route('/api/seed02/post', methods=['POST'])
def create_seed02():
    data = request.json
    required_keys = ['UN', 'Crop', 'CultivatedCrop', 'CropVariety', 'SeedSource', 'SeedlingPurchaseDate', 'SeedlingPurchaseType']
    if not all(key in data for key in required_keys):
        return jsonify({'error': '資料輸入失敗'}), 400
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO seed02 (UN, Crop, `CultivatedCrop`, `CropVariety`, `SeedSource`, `SeedlingPurchaseDate`, `SeedlingPurchaseType`) VALUES (%s, %s, %s, %s, %s, %s, %s)", (data['UN'], data['Crop'], data['CultivatedCrop'], data['CropVariety'], data['SeedSource'], data['SeedlingPurchaseDate'], data['SeedlingPurchaseType']))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'status': '資料輸入成功'}), 201

@app.route('/api/seed02/get', methods=['GET'])
def get_seed02():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM seed02")
    seed02 = cur.fetchall()
    cur.close()
    return jsonify(seed02)

@app.route('/api/seed02/<int:item_id>', methods=['DELETE'])
def delete_seed02(item_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM seed02 WHERE id = %s", [item_id]) 
    mysql.connection.commit()
    return jsonify({'status': 'Item deleted'}), 200

@app.route('/api/seed02/<int:id>', methods=['PUT'])
def update_seed(id):
    data = request.get_json()

    new_UN = data.get('UN')
    new_Crop = data.get('Crop')
    new_CultivatedCrop = data.get('CultivatedCrop')
    new_CropVariety = data.get('CropVariety')
    new_SeedSource = data.get('SeedSource')
    new_SeedlingPurchaseDate = data.get('SeedlingPurchaseDate')
    new_SeedlingPurchaseType = data.get('SeedlingPurchaseType')

    if any(value is None for value in [new_UN, new_Crop, new_CultivatedCrop, new_CropVariety, new_SeedSource, new_SeedlingPurchaseDate, new_SeedlingPurchaseType]):
        return jsonify({'error': 'Required data not provided in request'}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
                UPDATE seed02 SET 
                UN = %s, 
                Crop = %s, 
                CultivatedCrop = %s, 
                CropVariety = %s, 
                SeedSource = %s, 
                SeedlingPurchaseDate = %s,
                SeedlingPurchaseType = %s
                WHERE ID = %s
                """, 
                (new_UN, new_Crop, new_CultivatedCrop, new_CropVariety, new_SeedSource, new_SeedlingPurchaseDate, new_SeedlingPurchaseType, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'status': 'Seed record updated'}), 200

#seed02











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





