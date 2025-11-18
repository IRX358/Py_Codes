# Global fund setup
FUND_POOL = 1000000

class Treasury:
    def __init__(self):
        global FUND_POOL
        self._allocated = 0
        self._ministers = {}

    def show(self):
        global FUND_POOL
        print("[Treasury] Total: ₹{}, Allocated: ₹{}".format(FUND_POOL, self._allocated))

    def _add_funds(self, amt):
        global FUND_POOL
        FUND_POOL += amt
        print("[Treasury] Added ₹{}".format(amt))

    def _allocate(self, mid, amt):
        global FUND_POOL
        if mid not in self._ministers:
            raise Exception("Minister ID {} not found!".format(mid))
        if amt > (FUND_POOL - self._allocated):
            raise Exception("Insufficient funds!")
        self._ministers[mid].wallet += amt
        self._allocated += amt
        print("[Allocated] ₹{} to Minister {}".format(amt, mid))

    def _register(self, minister):
        self._ministers[minister.pid] = minister
        print("[Registered] Minister {} ({})".format(minister.name, minister.pid))


class Person:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name


class Minister(Person):
    def __init__(self, pid, name):
        Person.__init__(self, pid, name)
        self.wallet = 0

    def request(self, treasury, amt):
        try:
            treasury._allocate(self.pid, amt)
        except Exception as e:
            print("[Request Failed] {}".format(e))

    def check(self):
        print("[{}] Wallet: ₹{}".format(self.name, self.wallet))


class SuperiorBody(Person):
    def __init__(self, pid, name, treasury):
        Person.__init__(self, pid, name)
        self.treasury = treasury

    def add(self, amt):
        self.treasury._add_funds(amt)

    def allocate(self, mid, amt):
        try:
            self.treasury._allocate(mid, amt)
        except Exception as e:
            print("[Allocation Error] {}".format(e))

    def reg(self, IrSn):
        self.treasury._register(IrSn)


# ----- Let's run n see now -----
IR = Treasury()
AD = SuperiorBody("SB1", "AdminCore", IR)

IrSn1 = Minister("M01", "IR")
IrSn2 = Minister("M02", "Sn")

AD.reg(IrSn1)
AD.reg(IrSn2)

IR.show()

IrSn1.request(IR, 300000)
IrSn2.request(IR, 200000)

IrSn1.check()
IrSn2.check()
IR.show()

AD.add(500000)
IR.show()

IrSn1.request(IR, 2000000)  # This shld fail broo : overdraw
ghost = Minister("M99", "Ghost")
ghost.request(IR, 10000)    # shld fail broo : not registered