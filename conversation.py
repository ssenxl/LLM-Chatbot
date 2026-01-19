# conversation.py
from rag_engine import ask_it

USER_CONTEXT = {}

def get_context(user_id: str):
    USER_CONTEXT.setdefault(user_id,{
        "menu_level":0,
        "menu_group":None,
        "current_topic":None
    })
    return USER_CONTEXT[user_id]

def erp_menu_root():
    return "ต้องการทำอะไรใน ERP:\n1) PR\n2) PO"

def erp_menu_pr():
    return "งานเกี่ยวกับ PR:\n1) เปิด PR\n2) แก้ไข PR\n3) ยกเลิก PR"

def erp_menu_po():
    return "งานเกี่ยวกับ PO:\n1) เปิด PO\n2) แก้ไข PO\n3) ยกเลิก PO"

def chat(user_id: str, text: str):
    ctx = get_context(user_id)
    t = text.lower().strip()

    if t=="erp":
        ctx["menu_level"]=1
        return {"answer":erp_menu_root()}

    if ctx["menu_level"]==1:
        if t in ["1","pr"]:
            ctx["menu_level"]=2
            ctx["menu_group"]="pr"
            return {"answer":erp_menu_pr()}
        if t in ["2","po"]:
            ctx["menu_level"]=2
            ctx["menu_group"]="po"
            return {"answer":erp_menu_po()}

    if ctx["menu_level"]==2:
        ctx["menu_level"]=0
        if ctx["menu_group"]=="pr":
            return ask_it(f"{['','เปิด','แก้ไข','ยกเลิก'][int(t)]} pr")
        if ctx["menu_group"]=="po":
            return ask_it(f"{['','เปิด','แก้ไข','ยกเลิก'][int(t)]} po")
    

    return ask_it(text)
