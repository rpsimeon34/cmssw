import FWCore.ParameterSet.Config as cms

# This cff file is based off of the L1T Phase-2 Menu group using
# the process name "REPR"

# RCT - l1tPhase2RCTEmulatorProducer
from L1Trigger.L1CaloTrigger.l1tPhase2RCTEmulatorProducer_cfi import *

# GCTB - l1tPhase2GCTEmulatorProducer
from L1Trigger.L1CaloTrigger.l1tPhase2GCTEmulatorProducer_cfi import *

# HF - l1tPhase2HFEmulatorProducer
from L1Trigger.L1CaloTrigger.l1tPhase2HFEmulatorProducer_cfi import *

# DMX (just takes HGCAL hits and formats them for MHH, since there's no multiplexing in emulator) - l1tPhase2L1DMXEmulator
from L1Trigger.L1CaloTrigger.l1tPhase2L1DMXEmulator_cfi import *

# MHH - l1tPhase2L1MHHEmulator
from L1Trigger.L1CaloTrigger.l1tPhase2L1MHHEmulator_cfi import *
l1tPhase2L1MHHEmulator.inputLinks = cms.VInputTag(
        cms.InputTag("", "")
)

# GCTSum (only one card for now) - l1tPhase2L1GCTSumEmulator
from L1Trigger.L1CaloTrigger.l1tPhase2L1GCTSumEmulator_cfi import *
l1tPhase2L1GCTSumEmulator.inputLinks = cms.VInputTag(
        cms.InputTag("", "")
)

l1tPhase2CaloL1 = cms.Sequence(
        l1tPhase2RCTEmulatorProducer *
        l1tPhase2GCTEmulatorProducer *
        l1tPhase2HFEmulatorProducer *
        l1tPhase2L1DMXEmulator *
        l1tPhase2L1MHHEmulator *
        l1tPhase2L1GCTSumEmulator
)
