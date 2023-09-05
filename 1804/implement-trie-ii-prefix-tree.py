# 這題比較難：erase 要怎麼處理。要在 dict 記錄「下面用了幾次」
class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c in trie:
                trie[c][1] += 1
            else:
                trie[c] = [{}, 1]
            trie = trie[c][0]
        if "end" in trie:
            trie["end"] += 1
        else:
            trie["end"] = 1

    def countWordsEqualTo(self, word: str) -> int:
        trie = self.trie
        for c in word:
            if c not in trie: return 0
            trie = trie[c][0]
        if "end" in trie:
            return trie["end"]
        else: return 0

    def countWordsStartingWith(self, prefix: str) -> int:
        trie = self.trie
        ans = 0
        for c in prefix:
            if c not in trie: return 0
            ans = trie[c][1]
            trie = trie[c][0]
        return ans

    def erase(self, word: str) -> None:
        # print("erase", word)
        # print(self.trie)
        trie = self.trie
        for c in word:
            trie[c][1] -= 1
            trie = trie[c][0]
        trie["end"] -= 1
        # print(self.trie)
        return
# case 51/78: [[],["bp"],["ypg"],["uh"],["t"],["bp"],["hylma"],["q"],["i"],["le"],["biywd"],["t"],["u"],["hylma"],["agoa"],["aq"],["s"],["nslu"],["dbi"],["m"],["f"],["e"],["si"],["i"],["aq"],["oonmr"],["f"],["nxpwu"],["jtx"],["ooqb"],["aq"],["bj"],["u"],["su"],["oonmr"],["xgls"],["dc"],["nww"],["skksv"],["ivomo"],["tw"],["ttzgj"],["nsluj"],["ma"],["qridy"],["dbi"],["xgls"],["a"],["bj"],["iupom"],["agoa"],["am"],["ttzgj"],["agoa"],["htkog"],["bj"],["jlcei"],["ndxzb"],["ma"],["nsluj"],["htkog"],["gjihm"],["chsg"],["qridy"],["b"],["tth"],["p"],["i"],["z"],["am"],["su"],["s"],["vuaz"],["ipph"],["tth"],["oonmr"],["y"],["l"],["am"],["fjr"],["agoa"],["q"],["n"],["nxpwu"],["txbp"],["kbb"],["saido"],["kbb"],["lzfcd"],["bcw"],["saido"],["xgls"],["xy"],["d"],["lrr"],["lrr"],["ryls"],["sqj"],["d"],["el"],["p"],["s"],["xtpeg"],["htkog"],["vzwp"],["s"],["ivomo"],["kaeh"],["gsflr"],["t"],["ge"],["l"],["sezdm"],["y"],["gedcj"],["led"],["nn"],["riiuc"],["e"],["xy"],["si"],["f"],["njhh"],["xtpeg"],["gedcj"],["jlcei"],["sqj"],["ttzgj"],["skksv"],["y"],["am"],["aq"],["zi"],["txbp"],["zi"],["ttzgj"],["ttzgj"],["xgls"],["ut"],["y"],["wdv"],["t"],["jrcy"],["f"],["r"],["kaeh"],["subvh"],["xy"],["xtpeg"],["twba"],["f"],["xtpe"],["lrr"],["u"],["bcwx"],["uv"],["c"],["i"],["xnxy"],["ttzgj"],["su"],["b"],["dztwa"],["l"],["a"],["pu"],["a"],["l"],["ys"],["b"],["ypg"],["cs"],["dfi"],["q"],["i"],["dbi"],["t"],["gsflr"],["t"],["riiuc"],["wdv"],["htkog"],["l"],["txbp"],["subvh"],["rylsi"],["kjb"],["subvh"],["jlcei"],["wdv"],["eq"],["njhh"],["y"],["vzwp"],["rd"],["chsg"],["am"],["r"],["a"],["iupom"],["nn"],["q"],["y"],["o"],["osxu"],["kaeh"],["r"],["ws"],["z"],["wxpc"],["b"],["vu"],["dc"],["p"],["ut"],["tth"],["gedcj"],["ek"],["rd"],["y"],["gsflr"],["jtx"],["am"],["epb"],["led"],["tth"],["cs"],["osxu"],["iovrz"],["dbi"],["u"],["bcwx"],["bj"],["wdv"],["kji"],["bcwx"],["skksv"],["y"],["j"],["wdv"],["w"],["epbs"],["riiuc"],["qt"],["i"],["wd"],["oxwm"],["am"],["pmnj"],["led"],["lg"],["aei"],["a"],["g"],["rylsi"],["biywd"],["s"],["y"],["sezdm"],["brnzz"],["t"],["wxpc"],["hylma"],["iupom"],["ypqq"],["f"],["lrr"],["brnzz"],["sqj"],["biywd"],["eq"],["el"],["xy"],["n"],["qridy"],["chsg"],["kaeh"],["jkqfe"],["sj"],["n"],["biywd"],["bcf"],["i"],["riiu"],["ys"],["cs"],["lrr"],["qhjy"],["nn"],["y"],["wxp"],["iovrz"],["wx"],["hog"],["chsg"],["bs"],["qhj"],["brnzz"],["tt"],["cs"],["iz"],["q"],["c"],["nsluj"],["ndx"],["htk"],["uhfd"],["u"],["gedcj"],["kaeh"],["fjroo"],["liu"],["nsluj"],["pmnj"],["gjihm"],["si"],["bp"],["kjbys"],["bp"],["i"],["gv"],["uvf"],["cs"],["cs"],["sezdm"],["kaeh"],["y"],["jkqfe"],["i"],["d"],["chsg"],["rlvtq"],["f"],["am"],["iovrz"],["an"],["tth"],["pmnj"],["u"],["gedcj"],["dc"],["nsluj"],["q"],["x"],["dbi"],["oxwm"],["puw"],["y"],["bcf"],["gsflr"],["si"],["n"],["ut"],["gsflr"],["b"],["tt"],["bj"],["xgls"],["vg"],["xtpeg"],["aei"],["y"],["biywd"],["txbp"],["si"],["lzfcd"],["tt"],["ypq"],["ypq"],["tt"],["su"],["y"],["jtx"],["bcf"],["a"],["ws"],["nn"],["fn"],["q"],["y"],["r"],["puw"],["u"],["sqj"],["nw"],["htk"],["xnxy"],["n"],["ek"],["pmnj"],["vzwp"],["io"],["y"],["su"],["xtpeg"],["p"],["tw"],["ys"],["qridy"],["d"],["iupom"],["xy"],["sj"],["rd"],["an"],["dfi"],["gedcj"],["ma"],["nww"],["oxwm"],["subvh"],["xtpeg"],["qri"],["xtpeg"],["ypqq"],["gedcj"],["f"],["xnxy"],["wlw"],["i"],["y"],["eq"],["kji"],["gt"],["wlw"],["fjroo"],["ndxzb"],["vuaz"],["ut"],["zi"],["bs"],["u"],["d"],["bj"],["i"],["v"],["puw"],["vuaz"],["xtpeg"],["bcwx"],["ys"],["fjroo"],["n"],["dztwa"],["ndxzb"],["u"],["biywd"],["htko"],["fjroo"],["ek"],["ivomo"],["nn"],["qt"],["dz"],["an"],["twb"],["brnzz"],["led"],["aq"],["w"],["nsluj"],["sj"],["biywd"],["vg"],["uhfd"],["ek"],["ek"],["ch"],["x"],["s"],["k"],["rd"],["s"],["iollo"],["bj"],["u"],["si"],["f"],["ut"],["ipph"],["hylma"],["subvh"],["iupom"],["bcf"],["rd"],["dc"],["njh"],["kjbys"],["wxpc"],["y"],["q"],["an"],["iovrz"],["vuaz"],["qt"],["i"],["gv"],["rlvt"],["u"],["qhjyz"],["fn"],["u"],["nslu"],["iupom"],["a"],["iupom"],["qridy"],["y"],["l"],["si"],["ooqb"],["nxpwu"],["nsluj"],["nxpwu"],["aei"],["u"],["twba"],["s"],["b"],["dfi"],["jtx"],["jkqfe"],["jtx"],["lrr"],["sqj"],["fjroo"],["d"],["gsf"],["fn"],["qhjy"],["subvh"],["ut"],["jrcyv"],["sqj"],["eq"],["ek"],["kji"],["sj"],["eq"],["ndxzb"],["ooqb"],["aei"],["dbi"],["epbs"],["ivo"],["t"],["saido"],["txbp"],["dbi"],["dztw"],["puw"],["rylsi"],["an"],["y"],["biywd"],["iupo"],["dbi"],["kji"],["io"],["lzfcd"],["biywd"],["y"],["n"],["dbi"],["txbp"],["gjihm"],["t"],["f"],["gsflr"],["ws"],["nxpwu"],["q"],["w"],["iupom"],["s"],["ek"],["skksv"],["y"],["agoa"],["gjihm"],["qri"],["biyw"],["ws"],["w"],["b"],["d"],["uhfd"],["nsluj"],["lrr"],["ek"],["ys"],["s"],["an"],["iov"],["gsflr"],["aq"],["u"],["li"],["qhjyz"],["dc"],["kji"],["bcwx"],["b"],["led"],["gt"],["y"],["bcwx"],["hylm"],["y"],["oonmr"],["i"],["n"],["sqj"],["ma"],["dfi"],["l"],["ipph"],["zi"],["u"],["m"],["njhh"],["rlvtq"],["qhjyz"],["izsf"],["y"],["led"],["wd"],["ns"],["f"],["y"],["bp"],["ago"],["a"],["bcf"],["qtfex"],["k"],["oxwm"],["ypg"],["sqj"],["ek"],["s"],["q"],["kjbys"],["a"],["biy"],["kji"],["ws"],["x"],["xtpeg"],["iupom"],["b"],["r"],["xnxy"],["ep"],["p"],["an"],["bp"],["liu"],["pmnj"],["wdv"],["u"],["i"],["gsflr"],["b"],["a"],["gv"],["n"],["txbp"],["ut"],["eq"],["t"],["fjroo"],["fjroo"],["twba"],["bp"],["wl"],["jrc"],["a"],["aq"],["ek"],["wdv"],["tt"],["led"],["io"],["kji"],["uh"],["gsflr"],["vg"],["d"],["l"],["aei"],["qhjyz"],["ivomo"],["izsf"],["ws"],["ws"],["qridy"],["bs"],["ypqq"],["nn"],["y"],["wxpc"],["qt"],["y"],["ypg"],["aei"],["cs"],["xgls"],["rd"],["subvh"],["dbi"],["ipph"],["sqj"],["gt"],["kbb"],["rylsi"],["kbb"],["n"],["n"],["ma"],["bp"],["tt"],["txbp"],["agoa"],["skksv"],["am"],["s"],["sj"],["ivomo"],["b"],["hylma"],["gsflr"],["ioll"],["jt"],["n"],["kgagf"],["xnxy"],["s"],["hog"],["wxpc"],["m"],["gsflr"],["sj"],["aei"],["bp"],["qt"],["ttzgj"],["lrr"],["gvw"],["ut"],["vg"],["si"],["ws"],["n"],["jlcei"],["eq"],["txbp"],["tt"],["txbp"],["led"],["i"],["r"],["xtpeg"],["tt"],["b"],["x"],["fn"],["gedcj"],["g"],["kji"],["el"],["kji"],["ndxzb"],["s"],["e"],["lrr"],["d"],["el"],["kjbys"],["fn"],["wdv"],["i"],["r"],["dbi"],["sezd"],["n"],["an"],["sj"],["s"],["n"],["rlv"],["nxpwu"],["t"],["jtx"],["a"],["bj"],["ht"],["a"],["biywd"],["i"],["s"],["n"],["wxpc"],["ma"],["vg"],["bj"],["izsf"],["k"],["gjih"],["iu"],["f"],["i"],["y"],["g"],["ndxzb"],["liu"],["g"],["ws"],["puw"],["epbs"],["txbp"],["xnxy"],["xtpeg"],["r"],["a"],["rd"],["iollo"],["i"],["twba"],["qhjyz"],["p"],["agoa"],["d"],["oxw"],["zi"],["jtx"],["fn"],["sj"],["kgagf"],["eq"],["f"],["eq"],["f"],["df"],["d"],["gt"],["lrr"],["xnxy"],["qrid"],["n"],["g"],["n"],["njh"],["vg"],["k"],["ivomo"],["o"],["gt"],["gjihm"],["x"],["puw"],["a"],["y"],["f"],["ivomo"],["biywd"],["jk"],["gjihm"],["wdv"],["l"],["sezdm"],["jtx"],["iupom"],["xtpeg"],["xy"],["s"],["f"],["jtx"],["puw"],["i"],["sez"],["epbs"],["tth"],["bp"],["jrcyv"],["ndxzb"],["n"],["skks"],["kaeh"],["n"],["izsf"],["oonmr"],["zi"],["n"],["ivom"],["epbs"],["i"],["p"],["ypqq"],["q"],["pmnj"],["jkqfe"],["xgls"],["kbb"],["lg"],["kji"],["gedc"],["osxu"],["b"],["jtx"],["bs"],["bcwx"],["jlcei"],["qhjyz"],["xy"],["xgls"],["nn"],["bj"],["wxpc"],["i"],["si"],["led"],["osx"],["k"],["qtfe"],["cs"],["xtpeg"],["kaeh"],["epbs"],["gt"],["rylsi"],["oxwm"],["fn"],["zi"],["lzfcd"],["g"],["chsg"],["dztwa"],["xg"],["osxu"],["y"],["wlw"],["liu"]]

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
