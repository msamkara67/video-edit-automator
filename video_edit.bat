@echo off
setlocal EnableExtensions

set "ROOT_DIR=%~dp0"
set "INPUT_VIDEO=MySource.mp4"
set "OUTPUT_VIDEO=MyResult.mp4"
set "BGM_FILE=bgm.wav"
set "SPEED_FACTOR=4"
set "MUTE_ORIGINAL=true"
set "BGM_START_S=0"
set "BGM_END_S="

set "INPUT_PATH=%ROOT_DIR%%INPUT_VIDEO%"
set "OUTPUT_PATH=%ROOT_DIR%%OUTPUT_VIDEO%"
set "BGM_PATH=%ROOT_DIR%%BGM_FILE%"
set "CAP_FILE=%ROOT_DIR%_captions.tmp"

if exist "%CAP_FILE%" del "%CAP_FILE%" >nul 2>&1

>>"%CAP_FILE%" echo 0^|10^|User enters the date.
>>"%CAP_FILE%" echo 15^|88^|Fetch daily coin metrics from the Binance API -^> template workbook.
>>"%CAP_FILE%" echo 88^|110^|Transfer data -^> main workbook.
>>"%CAP_FILE%" echo 111^|128^|Convert to presentation workbook + add VBA to update charts.
>>"%CAP_FILE%" echo 129^|135^|Open the presentation workbook.
>>"%CAP_FILE%" echo 136^|166^|Dynamic indicator charts per coin (powered by Binance API).
>>"%CAP_FILE%" echo 167^|176^|Virtual investing simulation page.
>>"%CAP_FILE%" echo 177^|187^|Per-coin indicator table for filtering signals.

set "INPUT_VIDEO=%INPUT_PATH%"
set "OUTPUT_VIDEO=%OUTPUT_PATH%"
set "BGM_FILE=%BGM_PATH%"
set "CAP_FILE=%CAP_FILE%"
set "SPEED_FACTOR=%SPEED_FACTOR%"
set "MUTE_ORIGINAL=%MUTE_ORIGINAL%"
set "BGM_START_S=%BGM_START_S%"
set "BGM_END_S=%BGM_END_S%"

pushd "%ROOT_DIR%"
python "%ROOT_DIR%final_vid_edit.py"

rem küçük bir bekleme ve temp dosyasını zorla sil
timeout /t 1 >nul
if exist "%CAP_FILE%" del /f /q "%CAP_FILE%" >nul 2>&1

popd
pause
endlocal


