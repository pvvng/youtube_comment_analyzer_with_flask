stopword = {
    '에 대해', '팔', '하기때문에', '퉤', '잇따라', '하면서', '한적이있다', '그때', '입각하여', '시키다', '하면된다', '가령', '아', '와아', '자기', '와 같은 사람들', '인듯하다', '응당', '얼마큼', '얼마든지', '흥', 
    '반드시', '이로인하여', '와르르', '총적으로보면', '관해서는', '일단', '붕붕', '관계없이', '의지하여', '이 정도의', '당신', '아이', '게다가', '당장', '자마자', '말하자면', '더라도', '어째서', '그래도', '한마디', 
    '어떤것', '하하', '어때', '생각한대로', '그렇지', '다소', '아울러', '그리하여', '아니', '아이구', '이때문에', '하곤하였다', '어느 년도', '둘', '차라리', '관하여', '를', '습니까', '잠시', '향하여', '할 지경이다', 
    '삐걱거리다', '하자마자', '바꾸어말하자면', '여러분', '도착하다', '비추어 보아', '하기에', '각', '얼마나', '바와같이', '을', '쿵', '다수', '콸콸', '끼익', '줄은몰랏다', '하는것이낫다', '다른방면으로', '어느곳', 
    '어느쪽', '어떠한', '으로서', '이만큼', '여기', '이래', '저기', '하든지', '가까스로', '주룩주룩', '너희들', '한켠으로는', '예를들자면', '령', '요만한것', '하겠는가', '불구하고', '할지라도', '타인', '임에틀림없다', 
    '그렇지만', '여덟', '같이', '흐흐', '해요', '셋', '고로', '이젠', '지말고', '하기는한데', '얼마만큼', '이곳', '이었다', '아이쿠', '각자', '하지않도록', '이럴정도로', '하여금', '비로소', '딱', '실로', '이', '거니와', 
    '딩동', '자기집', '하도록시키다', '물론', '까닭으로', '뒤따라', '동시에', '어떻게', '막론하고', '의해', '과', '그에 따르는', '소생', '할수있어', ' 첫번째로', '삼', '힘입어', '우리', '로', '아무거나', '그러나', '너희', 
    '잠깐', '이 되다', '할때', '만이 아니다', '라 해도', '하도록하다', '곧', '줄은모른다', '고려하면', '비슷하다', '어이', '하기보다는', '예컨대', ' 참나', '어느', '이것', '구체적으로', '에', '마음대로', '바꾸어서말하면', 
    '저쪽', '이러한', '전자', '즉시', '된이상', '만은 아니다', '이어서', '기준으로', '어떤것들', '의해되다', '일때', '놀라다', '총적으로 말하면', '앞의것', '거바', '어기여차', '한다면', '알수있다', '구토하다', '더욱이는', 
    '이와 같은', '하고있다', '에달려 있다', '무엇때문에', '갖고말하자면', '이르기까지', '영', '다음으로', '마저도', '좀', '여', '다만', '대하면', '여섯', '도달하다', '이상', '아래윗', '이천구', '만약에', '예', '오', 
    '오로지', '윙윙', '한항목', '하는편이낫다', '겸사겸사', '그럼', '반대로', '게우다', '할뿐', '년', '시작하여', '오히려', '때가 되어', '안 그러면', '이천칠', '본대로', '저', '다음', '어찌하여', '연관되다', '심지어', 
    '일지라도', '이천팔', '봐라', '해서는 안된다', '아이고', '만 못하다', '하는 김에', '일것이다', '근거하여', '헐떡헐떡', '앗', '하려고하다','이러이러하다', '마저', '헉헉', '어쨋든', '그저', '더욱더', '뿐만아니라', '누구', 
    '그래', '때', '아야', '봐', '얼마', '어찌됏든', '오자마자', '인젠', '네', '동안', '툭', '끙끙', '등', '버금', '우르르', '그렇지 않다면', '언젠가', '이유만으로', '이렇게되면', '그렇게 함으로써', '넷', '왜', '결국', 
    '아니나다를가', '아하', '한 까닭에', '근거로', '이봐', '하고있었다', '아홉', '주저하지 않고', '여차', '어찌하든지', '대로 하다', '저것만큼', '대하여', '더구나', '즈음하여', '해도좋다', '겨우', '어찌됏어', '아니면', '또한', 
    '하지마라', '만큼', '어디', '어느때', '비길수없다', '연이서', '들', '할줄알다', '하면할수록', '진짜로', '자신', '따라', '솨', '로써', '것과 같이', '아무도', '좋아', '휴', '정도에 이르다', '하도다', '할만하다', '하구나', 
    '대해서', '논하지 않다', '메쓰겁다', '모', '무릎쓰고', '훨씬', '전부', '이렇게말하자면', '그러면', '몇', '한 이유는', '얼마간', '옆사람', '만약', '까악', '것', '뿐만 아니라', '총적으로', '어', '오직', '나머지는', '영차', 
    '얼마 안 되는 것', '만일', '말할것도 없고', '남짓', '쳇', '해도된다', '어느해', '하마터면', '할지언정', '요만큼', '약간', '기대여', '쾅쾅', '비걱거리다', '참', '이와 반대로', '하게될것이다', '매', '그런즉', '이밖에', 
    '이렇구나', '조금', '하느니', '무렵', '졸졸', '설마', '하는것만못하다', '의거하여', '뒤이어', '으로', '관계가있다', '부류의사람들', '마치', '혹은', '알았어', '할줄안다', '까지미치다', '하게하다', '든간에', '각각', 
    '우에종합한것과같이', '이번', '으로써', '했어요', '왜냐하면', '제외하고', '그럼에도', '불구하고', '그럼에도불구하고', '엉엉', '여전히', '틈타', '바꿔말하면', '에게', '설사', '퍽', '그들', '저희', '힘이있다', '응', '쪽으로', '어떤', 
    '결과에 이르다', '여보시오', '오르다', '각종', '일곱', '요만한걸', '꽈당', '아니었다면', '두번째로', '오호', '향하다', '설령', '지든지', '한다면몰라도', '할생각이다', '칠', '해봐요', '함께', '견지에서', '어쩔수없다', 
    '예하면', '저것', '너', '시각', '타다', '있다', '남들', '밖에안된다', '비록', '중에서', '허걱', '까지도', '하물며', '어찌', '에한하다', '점에서보아', '좍좍', '비하면', '더군다나', '무슨', '보는데서', '않기 위하여', 
    '조차', '어떻해', '소인', '기타', '그러므로', '입장에서', '다시말하면', '운운', '다시말하자면', '그위에', '뿐이다', '그리고', '그만이다', '무엇', '할수있다', '으로 인하여', '하나', '둥둥', '또', '하는바', '그러한즉', 
    '바꾸어서한다면', '더불어', '다음에', '이때', '그러니', '이용하여', '월', '반대로말하자면', '답다', '모두', '토하다', '결론을낼수있다', '일', '앞에서', '에있다', '한데', '통하여', '따위', '거의', '향해서', '바로', 
    '휘익', '및', '어느것', '하지않는다면', '이라면', '탕탕', '외에도', '하지만', '아니라면', '않기 위해서', '그', '보드득', '이지만', '공동으로', '여부', '요컨대', '헉', '단지', '하는것도', '그런까닭에', '보다더', '조차도', 
    '즉', '해야한다', '나', '된바에야', '할따름이다', '이외에도', '그렇지않으면', '일반적으로', '그래서', '누가알겠는가', '허', '관한', '기점으로', '구', '위하여', '위에서서술한바와같이', '중의하나', '형식으로쓰여', '펄렁', 
    '때문에', '아이야', '로부터', '의', '팍', '우선', '그런데', '매번', '따지지 않다', '자', '언제', '그러니까', '제각기', '개의치않고', '하더라도', '할망정', '것들', '삐걱', '이와 같다', '다른', '이와같다면', '상대적으로 말하자면', 
    '등등', '혼자', '육', '한 후', '야', '그치지않다', '그렇지않으면', '비교적', '에서', '하기만하면', '에 가서', '시초에', '예를들면', '습니다', '이쪽', '혹시', '이런', '바꾸어말하면', '부터', '하기위하여', '하지마', '시간', '와', 
    '사', '가', '륙', '의해서', '같다', '지만', '쉿', '하', '양자', '로 인하여', '관련이있다', '이외에', '이천육', '하여야', '대해말하자면', '제', '다섯', '그중에서', '허허', '전후', '까지', '이리하여', '이렇게많은것', '댕그', 
    '따라서', '우리들', '과연', '위해서', '뚝뚝', '불문하고', '그', '그런데', '으', '와', '오', '거', '결', '겸', '건', '리', '단', '뭐', '뭘', '안', '위', '함', '전', '나', '니', '두', '요', '더' , '도', '반', '별별', '별', 
    '짐', '딮', '딥', '언', '안', '셈', '명', '득','뭔', '걸', '봉', '션', '이면', '내야', '순', '종', '빼', '만', '수', '이곳도', '요즘', '히히히', '줄', '이거', '저거', '은', '는', '이', '가', '때문', '아래', '중', '능', '늘',
    '게', '내', '임', '진짜', '식', '번', '그냥', '분', '열', '알', '음','밖', '급', '꼭', '개', '앞', '뒤', '옆', '양', '땐', '오늘', '정말', '직접', '다자', '다시', '속', '말', '날', '킹', '구야', '마', '듯', '눈', '은줄', '이걸',
    '보고', '며칠', '며칠전', '몇일', '몇일전', '며칠후', '몇일후', '해', '온', '다면서', '위해', '저런', '이렇게', '저렇게', '해도', '왤케', '웰케', '왜이렇게', '작진', '거기', '님', '남', '얘', '예', '사람', '영상', '옴', '못', '젤',
    '보', '볼'
}