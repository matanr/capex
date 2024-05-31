#python train.py --config $CONFIG --work-dir $WORKDIR
python test.py $CONFIG $WORKDIR/latest.pth
cp -R ./work_dirs /storage/matanru/capex/$LOGDIR/