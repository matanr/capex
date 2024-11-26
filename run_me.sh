if [ "$TEST_ONLY" = "False" ]; then
    echo "TEST_ONLY is set to False, Starting training..."
    python train.py --config $CONFIG --work-dir $WORKDIR
else
    echo "TEST_ONLY is set to False, Skipping training."
fi
python test.py $CONFIG $WORKDIR/latest.pth
cp -R ./work_dirs /storage/matanru/capex/$LOGDIR/