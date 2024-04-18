def check_id_in_database(identifier, Id):
    try:
        result = Id.query.filter_by(id=identifier).first()
        return result is not None
    except Exception as e:
        print(f"Error checking id in database: {e}")
        return False
