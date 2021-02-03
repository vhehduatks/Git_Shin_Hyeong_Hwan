import librosa
import numpy as np
from sklearn.mixture import GaussianMixture as GMM

"""
1) 해당 프로그램은 실행시 .txt 생성 대신 5개의 예측결과가 콘솔창에서 한번에 출력되는 방식으로 작성했습니다.
2) 과제란에 올려주신 하위폴더 경로에 Training File(F1, F2.wav 등등)과 Test File(1, 2.wav)이 함께 있다고 판단하여 작성했습니다.
3) 혹시 기본 Load단계(1, 2)에서 입력 파일명의 변경이 필요한 경우, 1-(1)단계에서는 꼭 주석의 내용과 일치하는 화자의 음원을 넣어주세요.
4) 기본적으로 폴더경로와 입력파일명들을 조건에 맞게 세팅했지만, 프로그램 실행 전에 확인을 부탁드립니다.
"""

if __name__=="__main__":
    audio_path = r'C:\Users\140407\Desktop\Git_Shin_Hyeong_Hwan\KISTI_SOUND\\' # 절대경로 이용

    testFile = []
    speakerDict = {0:'F1', 1:'F2', 2:'M1', 3:'M2'}
    scoreTable = np.ones(4).astype(float) # [F1, F2, M1, M2]

    # 1-(1). Train File Load(16000Hz/16bits/Mono)
    audioTrainF1, srTrainF1 = librosa.load(audio_path + 'F1.wav', sr = 16000) # F1화자 음원 입력
    audioTrainF2, srTrainF2 = librosa.load(audio_path + 'F2.wav', sr = 16000) # F2화자 음원 입력
    audioTrainM1, srTrainM1 = librosa.load(audio_path + 'M1.wav', sr = 16000) # M1화자 음원 입력
    audioTrainM2, srTrainM2 = librosa.load(audio_path + 'M2.wav', sr = 16000) # M2화자 음원 입력

    # 1-(2). Test File Load
    audioTest1, srTest1 = librosa.load(audio_path + '1.wav', sr = 16000)
    audioTest2, srTest2 = librosa.load(audio_path + '2.wav', sr = 16000)
    audioTest3, srTest3 = librosa.load(audio_path + '3.wav', sr = 16000)
    audioTest4, srTest4 = librosa.load(audio_path + '4.wav', sr = 16000)
    audioTest5, srTest5 = librosa.load(audio_path + '5.wav', sr = 16000)

    # 2-(1). 각 화자 음성파일 MFCC 추출
    mfccF1 = np.transpose(librosa.feature.mfcc(y = audioTrainF1, sr = srTrainF1, n_mfcc = 24, n_fft = 512, hop_length = 512))
    mfccF2 = np.transpose(librosa.feature.mfcc(y = audioTrainF2, sr = srTrainF2, n_mfcc = 24, n_fft = 512, hop_length = 512))
    mfccM1 = np.transpose(librosa.feature.mfcc(y = audioTrainM1, sr = srTrainM1, n_mfcc = 24, n_fft = 512, hop_length = 512))
    mfccM2 = np.transpose(librosa.feature.mfcc(y = audioTrainM2, sr = srTrainM2, n_mfcc = 24, n_fft = 512, hop_length = 512))

    # 2-(2). Test File MFCC 추출
    testFile.append(np.transpose(librosa.feature.mfcc(y = audioTest1, sr = srTest1, n_mfcc = 24, n_fft = 512, hop_length = 512)))
    testFile.append(np.transpose(librosa.feature.mfcc(y = audioTest2, sr = srTest2, n_mfcc = 24, n_fft = 512, hop_length = 512)))
    testFile.append(np.transpose(librosa.feature.mfcc(y = audioTest3, sr = srTest3, n_mfcc = 24, n_fft = 512, hop_length = 512)))
    testFile.append(np.transpose(librosa.feature.mfcc(y = audioTest4, sr = srTest4, n_mfcc = 24, n_fft = 512, hop_length = 512)))
    testFile.append(np.transpose(librosa.feature.mfcc(y = audioTest5, sr = srTest5, n_mfcc = 24, n_fft = 512, hop_length = 512)))

    # 3. GMM 모델 구축 및 학습
    gmm_F1 = GMM(n_components = 5, max_iter = 200, covariance_type = 'tied').fit(mfccF1)
    gmm_F2 = GMM(n_components = 5, max_iter = 200, covariance_type = 'tied').fit(mfccF2)
    gmm_M1 = GMM(n_components = 5, max_iter = 200, covariance_type = 'tied').fit(mfccM1)
    gmm_M2 = GMM(n_components = 5, max_iter = 200, covariance_type = 'tied').fit(mfccM2)

    # 4. Test 및 결과 도출
    testSet = np.array(testFile)

    for i in range(5):
        for j in range(testSet.shape[1]):
            scoreTable[0] *= gmm_F1.score(np.transpose(testSet[i, j, :].reshape(-1, 1)))
            scoreTable[1] *= gmm_F2.score(np.transpose(testSet[i, j, :].reshape(-1, 1)))
            scoreTable[2] *= gmm_M1.score(np.transpose(testSet[i, j, :].reshape(-1, 1)))
            scoreTable[3] *= gmm_M2.score(np.transpose(testSet[i, j, :].reshape(-1, 1)))

        idx = np.argmax(scoreTable)
        print(speakerDict[idx])
        scoreTable[0:4] = 1.0
