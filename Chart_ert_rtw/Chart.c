/*
 * File: Chart.c
 *
 * Code generated for Simulink model 'Chart'.
 *
 * Model version                  : 1.1
 * Simulink Coder version         : 9.8 (R2022b) 13-May-2022
 * C/C++ source code generated on : Wed Oct 23 16:51:52 2024
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives:
 *    1. Execution efficiency
 *    2. RAM efficiency
 * Validation result: Not run
 */

#include "Chart.h"

/* Block signals and states (default storage) */
DW rtDW;

/* External inputs (root inport signals with default storage) */
ExtU rtU;

/* External outputs (root outports fed by signals with default storage) */
ExtY rtY;

/* Real-time model */
static RT_MODEL rtM_;
RT_MODEL *const rtM = &rtM_;

/* Model step function */
void Chart_step(void)
{
  /* Chart: '<Root>/Chart' */
  if (rtDW.is_active_c3_Chart == 0U) {
    rtDW.is_active_c3_Chart = 1U;

    /* Outport: '<Root>/C' incorporates:
     *  Inport: '<Root>/A'
     *  Inport: '<Root>/B'
     */
    rtY.C = rtU.A + rtU.B_g;
  } else {
    /* Outport: '<Root>/C' incorporates:
     *  Inport: '<Root>/A'
     *  Inport: '<Root>/B'
     */
    rtY.C = rtU.A + rtU.B_g;
  }

  /* End of Chart: '<Root>/Chart' */
}

/* Model initialize function */
void Chart_initialize(void)
{
  /* (no initialization code required) */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
