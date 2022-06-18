def on_forever():
    if mbit_Robot.Avoid_Sensor(mbit_Robot.enAvoidState.OBSTACLE):
        mbit_Robot.car_ctrl(mbit_Robot.CarState.CAR_BACK)
        basic.pause(1000)
        mbit_Robot.car_ctrl(mbit_Robot.CarState.CAR_RIGHT)
        basic.pause(1000)
    else:
        mbit_Robot.car_ctrl(mbit_Robot.CarState.CAR_RUN)
basic.forever(on_forever)
