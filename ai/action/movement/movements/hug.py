from time import sleep

from ai.action.movement.movements.basic import move_head


def hug(mars):
	mars.setHeadAngle(1, 0, 0.5)
	mars.setHeadAngle(2, 0, 0.5)
	sleep(0.5)
	mars.setLegAngle(1, 2, -45, 0.5)
	mars.setLegAngle(3, 2, -45, 0.5)
	mars.setLegAngle(1, 3, 0, 0.5)
	mars.setLegAngle(3, 3, 0, 0.5)
	sleep(0.5)
	mars.setLegAngle(2, 2, -90, 0.5)
	mars.setLegAngle(2, 3, -65, 0.5)
	mars.setLegAngle(4, 2, -90, 0.5)
	mars.setLegAngle(4, 3, -65, 0.5)
	sleep(0.5)
	move_head(mars)
