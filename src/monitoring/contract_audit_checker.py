async def check_audit_status(contract_address: str) -> dict:
    audit = await fetch_certik_audit(contract_address)
    return {"audited": audit["status"], "score": audit["score"]}
