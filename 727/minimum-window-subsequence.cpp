//先照 Editorial 方法 3 Greedy 寫, 但 testcase 49/68 長度 1萬 vs. 長度100, 太長超時
//10,000 * 100 * 10,000
//最後找到問題，讓used[i] 只記每一輪第1次出現的字母的位置，就好了
//"abcdebdde" "bde"
class Solution {
public:
    string minWindow(string s1, string s2) {
        vector<int> pos[26];
        for(int i=0; i<s1.length(); i++){
          char c = s1[i];
          pos[c-'a'].push_back(i);
        }
        //for(int i=0; i<5; i++){
        //    for(int now : pos[i]) printf("%d ", now);
        //    printf("\n");
        //}//印出pos[i]對照表, 與 Editorial 方法 3 相同

        int used[26] = {}; //對應 pos[i] 用過值, 就別再用
        int used0[26] = {}; //對應前一次用過的第1筆

        int bestLen = INT_MAX, bestStart, bestEnd;
        int prevGoodStart=-1, prevGoodEnd;
        for(int start = 0; start<s1.length(); start++){
            int now = start;
            int bad=0;
            if(start <= prevGoodStart) { 
                now = prevGoodEnd; //之前走過的還能用哦!
//printf("+");
            }else { //之前的不能用,只好重新找一次
                int changed[26]={};
                for(int i=0; i<s2.length(); i++){
                    char c = s2[i];
                    int good=0;
                    //for(int next : pos[c-'a']){
                    for(int k = used[c-'a']; k<pos[c-'a'].size(); k++) {
                        int next = pos[c-'a'][k];//這個字母的下一個位置
                        used[c-'a'] = k;
                        if(next>=now){ //找到字母下個合理位置, 太好了
                            if(i==0) prevGoodStart = next;
                            now = next +1;
                            good=1;
                            if(changed[c-'a']==0){
                                changed[c-'a']=1;
                                used0[c-'a']=k;
                            }
                            break;
                        }
                    }
                    if(good==0){ //沒有找到,太糟了
                        bad=1; //放棄這一輪
                    }
                }
                for(int i=0; i<26; i++) used[i] = used0[i];
            }
            if(bad==0){//有成功走完s2
//cout << s1.substr(start, now-start) << endl;
//printf("%d: %d %d\n", now-start, start, now);
//for(int i=0; i<26; i++){
//    printf("%c:%d ", i+'a', used0[i]);
//}
                //prevGoodStart = start;
                prevGoodEnd = now;
                if(now-start<bestLen) {
                    bestLen =  now-start;
                    bestStart = start;
                    bestEnd = now;
                }
            }else break;//prevGoodStart = -1;
        }
        if(bestLen==INT_MAX) return "";
        else return s1.substr(bestStart, bestLen);
    }
};
//case 49/68: "oinhgbydbkeobqttxjdxpapkmyuawkhtvfkvbygyhjgdymftztcixzkbsxvdymshbcvmutmebythigiyzubvmnunqhblfvvaqwbdmdhtytnftysttidwwfxizfdlgdccbjdqjjdxqzowfzcadnnsljorpqwjuzevcusaaqlfllovmdgbxyrzggyeysfaehtespilosyspotamntnnadsqdwajgtbqstkjcbtydtlckyseixzkrpzyspwzpmrdqpptkenfsyqrsioizempvdawrjotcplurkgzpjcagjovoogpnvvgbebmhlvjtyiemauwnfwlqahkvfvwbunijdxfjfdmkbkateoubbkrasmhtjvmqoirzivnwhusmupifrhhgznvbqprqjsfjkxxcevkfglmyptjmvicqkerhshnskufxayckcrleegusxffhipkevgmuvhgusihoafkfdtomzrberluusfrelsdfojudnjpgdnrcwhbamwpmlighsdouanrtasghyumsxvlqphpmzsholpqoupohjxijitkqmsqbxtntqofzdneqhxuiampossztkcciykugewoaoukyquafkmpkcbwhkbsfinjfoyxqzgchdbdqlcexyswxvzxthhpkzypwsdukzoetjvwibhiilqkfkihdafmuxexndmhgtcoftbbmhpjqqzzqabmeezsyfqxiezpodpwfkdfdughjkfizcwhxqlcvyvysgqrzujssirexmucronqlimuumtgrtwsjtdcexgualsfiezgkkmtdxcmchhcdjkqmmurbxcsbvvhpsrbrvezsxiigeiuedmoabsaanjmemrrnnchngkffbccizvhzwopfvhqmcumpyprvoirwqntqbiziuroayazqltzddfjjxthleljmtfvqbppxvcwdptnvdykyxzfwhcwgpdyjunwpfzzogsamebambujkxmhpttltqxceicluoihjxeufjuyvvikpcghtdgoqafybddvidulcgecclhitjyrgjdezvbacctwgqptydmumtfftbrhzoyjgtgdmugvfsrtrubazezokpmqtwgfopppqelaowvazpjtnupjiqoynbtibpmjscvthjadmbdkjvljzleknmdseiafiddeouewenwrflwyztqmddpvsuqniutwojnmssptvjsihxxjferepttiuayzakgffltlfdcxpknuwntvoecvvgwsdrgaicqpydzqvdvynwasrfmcupcbqefnedvskvgpspbvnzxcpauffnienatukmnzemqfsdpzquramqmgwhvriusavarhkxebpzwgadtgxvizsemugbfqhxdvktbrnbstokrsrylfqfiqjvclrlwotbjztktzbniphlngsblvosqfpjfjivpyxyyfycikynrtwdzywmeuhgvxkvzyqqmojfnevpqkqhyfrwmgwbufoaeggfcangvvqqzquigmoofuuhgysevemkpphmitmpeqwwfhvnmwntfgeavyjjvthyjhrpvoqinjmtjodiuguyhdgabczcbcmsbcszudedvzjxgrbdwvxlraoqtttuwcjzzthqqtxyxdxiatbgolfsksfguomsyhtttrpismnwxynrfcrzjgeltvemtxzdyxqhairdqnmcxnlsdcrafjykoffxykuheniwakuoigkpsspgsjtngepuxgzqpqypcdvlzbajznyjjynhwwiyemdvtnnpexufyscxenxrafdemzidvqgyrghghdicouykurbivwgudevftebwrxbshmmqhskntobgwkvxrpzotsyzqppsbdqaqspphsrqruyhdzxnfygofljcifwpibwamscrxfdutngvnbcajagbpggiasmnzgffmokasfvtnabsyabmxwflmtjjywgtljygzhjrouneylktzdcgtmzlwocswwmaahztluasrdseknwhtybwmfpmqutugekoeeldqowcihyeatvmygviacpshcghbrxsozdwujbsvhkhbumixsyivplaxlmixpnuvgushpcopbozjszzoeelqbuokdkrnvhbouzjfjjqmgqrtpmkemizbkoznhrxgaeorcfkzbwbrduwhfkvondzwuqxqjygbwnzqhgmazqtgdfvkmvdyvsdtukliapshsfqbaocnkccxtqeagkrllrlcdhfwavlznixhoemgtjnfuijfazwhlxwrgnlgbgvyfmsmpcimgywkfotphmtumxrgmxrotvsznzgugbkrzfyaztfyhzvmldyokwrdydrbfurjngcirngeufxmkjgsueehsluaoriqyijsbfbihkgdivcgtogebbxkmqwynqzuodjxluiyhugslxuxjpjghepaukxzqblxdidsffvavcijpprvtipxehwkmxsswmmrqamfzymsoadrduauuzsiiuoscleobozgpsmvbzdacurcfdalljohazkmzpajmnshizotgghbkurctovtgmfvikofjnqhkjoyxxhfslqztbtlbuwbyrxpapbumdtrknmlpbwktyyetploqnpqxfjsjnzwbdcfbcoqkghiporuokhddmjrplxhyyzlmtiaplrtnkqmfxxneikfjjxkabbuzurutffafgnxlknowscioaryktjzdaoxhubeeqboiordfsikikprozqflvhncsdsmamizuzprnydugvetsabfhndopbktvukfkrznrrnphawbqexmgaigyelqqokvnhclhwvmjdifyhiecdgcmmwtmiwamzjiqbekchnuajvrrskkkvpwltjcfuxwsmllhnfizrddbwfvcgosrtvwcgxhbegeyhodwfxwlukefkacorwyzbrnwpbydpcczcxyzmjapmezlxmzigvcjwqjsyojzcmyefgrwazomtmgdupwsszqaqkfrixydvebexxgocottblxxbvivsggoerquigpckaxraxcbadsaqpqeupwwbfplvxgtfcpezitmsbtytvnecuobripkaqcjdttnjnsmdxbnodubssnhgrqyeigmgufbvzktkqamzdlqvdondkhnitxhrxtggumnktoicglkewrsmpwvldbdqepnrzyhpqkvqnrwnvfdbvwmltqahuawqosdmvsutlsqjivimszeixhoabnkrhnegagnennkkargrnlcqiufjlgflkfoduwhbluwapbjsuyopdzjcxmpfqyucyamkuiqnvmgnbloebhqgrswyhfxwrlmfaaegjkycqbfglrnfydzurompggbmeydaxwzhrpjocscpnkradcogkjktcapwyedzovgxyrybhzqdsuwipajkxcycddwhmevhmaonabqmwklveourkoqydkqkeqpatjmvoelhdnaftfnbtiodcewzfmlglsvvadrewcwjtovstxjlbqhitosddsvqouutqxpcrbtebgptogatbierzrraxiequmvlkwunvbcrhhyvbdwktzfzkcjruokoizdoqyposusqpwerxxvmwfzzawgxueeckjtzeyohtzqkayorikgyhslhgkarekozmuosrdnlqewjuatowyjrmazefecixvtraofaevnjgghrvnoeslrxezekxzmrfpsyrulebsmkitblfsidxgfsppdbxnnbgfpvwqxvqdzxboprskfynslhnfsmwxzoiohwvumdsiuxagbxkqjqmdgwzdlzlgozvcnjecmyseunfxoiazvxyrmkbcicjnueffbyrlxsknylhavrbgddqqckfnkqmqhqlyeczvphffnnsojkoylyrxxieaybskgshkhrsstutnyupnjxutbqxobjfiqjgeinefgkpacjpgqryvktztwntxczehtlhnlbghfxfoegdcytuydnbzorlrgcuyzfkeovaimvuxubakyycipzxvpbmmfdzljvshcdsutkgdqjczwumzpdgfwtgrwfinsydfetahbnnyqchjprwaeyymcmqdoozoxvcwksvfssubhnnoadalbsscndvloplpezpkmkcrgdtjsjzokhwqclhdeyxkdpbedillhslncdgfbuwbfpfmmyulsmxjcadiqixcyzvwdpvieritmlixexfzxgylroenmgfpfqyywsrazkmuvedvyxhiappdflgcvqntiwltlhhelvwmsmgavjdnhcuvebcdfftjmwbslevfqxanzpxnzhoflifohqwcukcgpjlvyjeivfcpmmdrntnlgbcmgkrkhmtsuemnnamediexvqutycubpxpjydgxfrrimicrjzplnhfemhginzbeciaruobwtzshqyuzdryjqppuchmtgrctapexygcaueuenwgqskbrdmfxpwcrvdljzdbxdjjhcrocutfglfhnbkoesjfvdupyduwtexnbzvisdjzlibnpcnvbigiwcttatgzjhnrgtgmwyvqlbhevuhykkfqtgvpqnbsmtrfhsujmbjteaugxvwjctpibatuvnzvbvmlkiludeeepbxcmcyrzkqgayizxmwajogjwnwqpdkfirlvsxstamdtaupgfplcdmgdrfsnackeajbcattrpsgaclrzhowlknvgxexsczgiizbgxaehxlfxhpcmqoiotinxzeucvkqtarzsfkasipncxppoaknyzlgbnxqqvxgsmknpmbtnklecelypmkufmkhwvwwskhsmpdgexnoigucekzooxglevbonfcrjipnatqauhfzaeahbwuewxxvkhwnznbcqcvvjteohknckhtwnegkyszfxwscmxyoimgimtouzmbkllpelvkqgkyrhlbttufnlwjgudxeagqujhkytbqxjpltmyptlbmnansqmlecfrgbzpoutjyuxqodpjanjhytymhbsfohfhujsgogcwsheofsrghygwucyckiobxncyhniijodvwxlnbzcwjtlqplvdfyhrafyifnmelkiqxxdmvgixmmouzmcmtwhalmgbjoluynppyacgcqpeupjjxueetjzlgqjfyhsjtlmxtpnwexjzjagnjotneytncknwxnrrcdjgotmmrhipfwhplilicvkiilhttmaitlrlpngmxwyezxjioxhokxnumwjtgdyknrkhzdxoojyoimykfjoyuxjaqgwtetfeugzzqqmavqgzyrpbsqovnwlxdorqsbnbluouzqbchccdepxuyrwigxlskohykoeficzglbwflsxsozljzujsxtaxnigtvcunblmaikzudjtehwyavxmevhywhlvdnkebaereamgzxpzebxhoofohlqoqyfdsxvdygiydfzkcikhklahwxtmipxrrwqakhglvwyyoqcdknynkrqggggaosroeunlyucxuqabtovaoigigzqwwntnjrajvlxigxsxpnmmlwpwkfrdoegubdofujjrlfztrojmusrhopmxwhuaqxahkwoceutsziguuarblwzyqujffklmyponwbowihgmiuhteikoftuxsacoygwrpnxtxqviprdasbyxspqqbkqsnuntjwzmgdzccljfxcsucopxfxppajftmzjzighhaujyicyqgltajnfkgojizvjphpewjylawngmfoyjbrtnfxrfjafeuudvhwqsjpojljbrhcvuusotzgihwvxzvqgskvgkkiuwmihcqahacwxdazugitepdhikjfvlugcopbaijztmavhmfxnzluftcpbdphjiadidxhsbcijfsqsooimpytfwbxjoxoveyjnodpgxaifctcaszedrgnqgcjxxzlarmzinafoauyhgslimbbngvfdxfqlodpwqcyqogbnlhtfgegllxnwetwziriukmwdpfbqkfnhtqlpospqxkyntoqhwfrxonpiqyiixawrubojsypnevcobiejoctaaqiowefojfpdgifkxzlpgpxjubruheyczmbeimozbciizewbdhbgmalfdmuwmzhcydsssyeudsvgxqatadvywuxgkvhmrqbpvjinnbegfzlqxmkffztcumvlgdplmbbghejblzyhnedytjymqwfupmrzilxcqsriiiqpiqjwkfksznlxwxkwfavbzodkdsrgbikskyedgkqmxrldbmthvjrtaonrokgkqfoxsjazcfcrnfrlbvweupkebgjggksoswkvaogcwswgvxuqxzngxjncdrejxehkclidelowfpcebcmpxqbmawjupocfrfbhkdpxuxyyjdjnorssjgfugdyqvcoqyjvyuyuadwxsoozlhyrthymdqxdrcthrynnsaozqqcgoapgxlotajfvgjahofqinxxtaxlldkfpsraqykwdijqouofewxqioxgkaqhixzsojrlsdltdnwahmriumairurpxtwnswqnwdpufejtxdlvxrixybvwxvpqvhihyyentwmhdmizottygvuuulmogwdhlxqkythjwktokppjndiyfnqhxvwrrwpxcrdxmdenzwmfmscytjtblakqmwwemfeebozkpfzrlbhtipsvdlxskdumxomqxrsqkytjbhaozxfriwkeyghmthbdbemerxoejysmckadjdntigfdxqdokavggtoiqkxzdmbrosdnlxduxntquqcpjjjejswcimdybopasspcxnhbgsbihmtoylurwetfbvbtfekmxhjezsukehtirsmuwgrxmgcsiqcvhrpklslidryftbegxkuskajukbilbkkhtimhtxdonutgjjsgicwnxuehguzozqsxekabhkwbawtnrefwjkckohxswrgbsnazhusltrtuawgxefxhoojesvahtdfubjptvvgufukdykcmukfrqbtpbralwfctvjpjozmtuicilfjsubltacglmntgngctktznzohmsyqsuhjghchlrbqxqzornubucpnysnzkzxhxjjjwlphrgcgedocrpyezxyuqgiboplqflcultfnrvzvskgipjleolkvpcomxbolzyrxablzlcpfdivizgszwbuoiacervtagsbvxiaxzslcprinclvpdrdmqemhwocjclsgiwktijvrytjdiitodzrvdwkmvgjeoeabguucszoyznevhyjhuqcmfcukdhvuyqfckxiscltrcsrmcfuowtqflzezgbhjfpenijdkcmkxkkxbpgrdhwremkymjdywjtwyhkzsymxjeydworevwjiqepduxublbmmgfqkzxuryysixqcqnbrleusrtdqpxzkejewmlcrbdslwoxkkfxssdqrogvhqljzfdfgbtqczmjehreeesnjftwidqqrstrtxoeymdiinjxvojzxqjtveiuqhbwvjvvfrrakaaoggavpmitanmszvdrawepzdmboplgzpxatpyycecrxckigtmmhekbocrsazvcnmrolcomfrjycfllgzsfsoajnaheolwrkquawjywtpdhgsfguaxrlvoefywidxblvmvvdxsceeputcgjhteknmmkptaqyiirhhbzfjepazoyycgaebiqbnempcgeeunllkaevcbziuzhqhhhqwzfzcovegxawkyejdcmruoifyjqiegzmjqdenfmdvjxedeumdynffuysotyfbaqkphgqctidccujnrvuqwquxciazqxvhznbtzkfyqbnsldkqreeqkimmbppzhgigmpgyysnhitxkplcetbwaivntfnjwetxtmgklybdnbrzanaxqlfvfuuvxygwdtkmkxdxhtbjmsfnsroiclsyusgxfmjwrzxzovxicxiovepjbqxnfavyizdvkycaowadaxxzvufvqbsjpfkcwuhaynkgbksowxsxqtdpnzezqyykyslgrltobxtateoruymztykvyhlvevckxvenzolkogkhmlmibgygeqqbvjgyjyzzgkxhzonpscqbwnyhzznyecwjfxucggoiwhsonrwpgpsjpqxpiepawbryxakdadkuxbucwbutvweknarhyvlireyjqaxsxosobsdtkaiafjqemfimasexlxnrwcvxljuytdtnsjlutfuotcglmyagsnhotfjcxyogybumsvryiobejepgezjvnyvxkingeqvyeizlomzxmnayayjdcvqpixjjypqruikggmtrhizklpgnzyvfabquwomsjfejkwllsopnpjncnzusytglqxrvyckfoxztxjrghupfmpxwwlfgxzyjmqbcilysmmdlyobnwhdokiaztzarkzyycpgblmopbforuwdryyxlcrvmpykvgavonpquzlojbbzhnlpfdridbdkspodrevpzastczamhabphyeauwaoehoaaznyeqhaknwmkbufyloeazzxtzggorjpkoxjtpynhtebisefzkwyeyngntidvfgrsllrppduflcjrnfoolnbxbzlxcumocxotcpyqvbuppyxkukocohinudxivmbfoblolcthvlzelbjecwgdblmdgkelvkfkdtlxahcbggblxpiubyqpkfrphfqnebwholfnamvxuntbwvypjyuwjiwejmcxduhkqlqebhjbbgmffepyfodrugjoavoefjgyndqskchqatonzqjvxyrffxgsamyhucwaipynmsnqzstvldsdptyyphzxxvqfwseozoncyfdphscsflpbidrcfsppbkcigywlvhsvhioampfxpivvushocdwapgicwircsmammqsnmewoydvggnloeifuzsotaozflgzcfzdqlrtwaacfelzynemghnxmqmlmdpzwsgkvmmrkznbxcgirsioiynqubqgkcvbpdboqtwauuooqlzszntnxqwqpblqxaqhhcssjzbxsppedmkqbewookqzsnhjxbjupaxmemfgkozevgohkhxblheqxlgjpisgsffgbhdobzptameezhilgtvpychtzycmvavkeyjtkbgbszrnhpgojujvgztrltnqgcmblpxntulntlbljyqfcvhqpsuyalpwgimjkulnfyfgmswuatzgfcbmnvmpvatkaccqamgoaozbjslbxdklegezdkhsafqzonpohhqfvxjtkifrsimvpgyqrutanubgjeykwrygtkgbfobbyjdhynhwbcjlkjzxpaoseqhxuijebzlqghqhcvpnfmgjcjnlamgdwgmxpczxjykzqkrtgczgyajrznowbarqgdcwcfwkmakffwzqmkdkhavatmkncpsbmnvpidgdkifvngizdkyfbxcrestsoexyqvonwohrrhanfevcfmnovlxbaietvpikttexvluxkmbcxvegcnktxvaffextrxloyyhbvrkcudgutbzluebsfdmghadqijywmrynfxjoblljlkbsmsbdooxzotbzuqpyuwlcojbqqektooizlpoowmrjbrkobywfsxjyofkxiusptaionpzqmnchntrfhsrkxyaxampzznsbmsvypbclurxjpxxdpazttkxqejwapxsoxjlhibvctoegykwuollivrsquivjgsphkewcsonaknzwwtanatxdhexykzqxesvdcisbhrikgpkjumdhxljejvoaxyduwzrpgvszwpnfacwmpmdwpmloajfxwlgzjdkjtthslmwwkjuqioksvmeldrmyzfpvnxbuyopludwxdtgiywvfshzrtalqcnicvpdqoserbvtkhryymrjljhtnumyxclnkbpepzlzwshlhhxnrdlwpeqbboytjuwymxswhvzltdsatnweqnunpweuzxrnpnituresjuvgovcdjpgjlkmfcvdeyhojsyzqxvjyqaiceegpxhdquvykzvlibbxmiuddixwmmopsqllhscznmwruidfxoaorfsimvwrammbrqpeevuowahvyykypxpyx"
//"ldoubhquynioifnbsccgypfsqqbwygakxgqubmzpwdhwbznjcjjesusihwwvbkvjikceopltamlqmydwxrjzuoodbendwwbvpfss"
//case 56/68: 2萬字，22字, 單獨跑OK,但Submit時，就TLE 1555ms
//case 68/68: 
