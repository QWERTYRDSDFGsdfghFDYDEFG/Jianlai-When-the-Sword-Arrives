init -10 python:
    # Voice index: use stable IDs in scripts, map IDs -> actual file paths here.
    # Keep paths Ren'Py-friendly (forward slashes).
    VOICE_INDEX = {
        "voice.scn_0001_midnight_courtyard_return.lbp.0001": "audio/voice/scn_0001_midnight_courtyard_return/lbp/0001.mp3",
        "voice.scn_0001_midnight_courtyard_return.lbp.0002": "audio/voice/scn_0001_midnight_courtyard_return/lbp/0002.mp3",
        "voice.scn_0001_midnight_courtyard_return.lbp.0003": "audio/voice/scn_0001_midnight_courtyard_return/lbp/0003.mp3",
        "voice.scn_0001_midnight_courtyard_return.lbp.0004": "audio/voice/scn_0001_midnight_courtyard_return/lbp/0004.mp3",
        "voice.scn_0001_midnight_courtyard_return.lbp.0005": "audio/voice/scn_0001_midnight_courtyard_return/lbp/0005.mp3",
        "voice.scn_0002_midnight_lake.cds.0001": "audio/voice/scn_0002_midnight_lake/cds/0001.mp3",
        "voice.scn_0002_midnight_lake.cds.0002": "audio/voice/scn_0002_midnight_lake/cds/0002.mp3",
        "voice.scn_0002_midnight_lake.cds.0003": "audio/voice/scn_0002_midnight_lake/cds/0003.mp3",
        "voice.scn_0002_midnight_lake.lbp.0001": "audio/voice/scn_0002_midnight_lake/lbp/0001.mp3",
        "voice.scn_0003_lihuai.lh.0001": "audio/voice/scn_0003_lihuai/lh/0001.mp3",
        "voice.scn_0004_word_youth_elder_night.lh.0001": "audio/voice/scn_0004_word_youth_elder_night/lh/0001.mp3",
        "voice.scn_0004_word_youth_elder_night.lh.0002": "audio/voice/scn_0004_word_youth_elder_night/lh/0002.mp3",
        "voice.scn_0004_word_youth_elder_night.lh.0003": "audio/voice/scn_0004_word_youth_elder_night/lh/0003.mp3",
        "voice.scn_0004_word_youth_elder_night.lh.0004": "audio/voice/scn_0004_word_youth_elder_night/lh/0004.mp3",
        "voice.scn_0004_word_youth_elder_night.lh.0005": "audio/voice/scn_0004_word_youth_elder_night/lh/0005.mp3",
        "voice.scn_0004_word_youth_elder_night.sr.0001": "audio/voice/scn_0004_word_youth_elder_night/sr/0001.mp3",
        "voice.scn_0004_word_youth_elder_night.zl.0001": "audio/voice/scn_0004_word_youth_elder_night/zl/0001.mp3",
        "voice.scn_0004_word_youth_elder_night.zl.0002": "audio/voice/scn_0004_word_youth_elder_night/zl/0002.mp3",
        "voice.scn_0005_du_klakeduet.narr.0001": "audio/voice/scn_0005_du_klakeduet/narr/0001.mp3",
        "voice.scn_0006_peiqian3.cds.0001": "audio/voice/scn_0006_peiqian3/cds/0001.mp3",
        "voice.scn_0006_peiqian3.cds.0002": "audio/voice/scn_0006_peiqian3/cds/0002.mp3",
        "voice.scn_0006_peiqian3.cds.0003": "audio/voice/scn_0006_peiqian3/cds/0003.mp3",
        "voice.scn_0006_peiqian3.cds.0004": "audio/voice/scn_0006_peiqian3/cds/0004.mp3",
        "voice.scn_0006_peiqian3.cds.0005": "audio/voice/scn_0006_peiqian3/cds/0005.mp3",
        "voice.scn_0006_peiqian3.cds.0006": "audio/voice/scn_0006_peiqian3/cds/0006.mp3",
        "voice.scn_0006_peiqian3.cds.0007": "audio/voice/scn_0006_peiqian3/cds/0007.mp3",
        "voice.scn_0006_peiqian3.cds.0008": "audio/voice/scn_0006_peiqian3/cds/0008.mp3",
        "voice.scn_0006_peiqian3.cds.0009": "audio/voice/scn_0006_peiqian3/cds/0009.mp3",
        "voice.scn_0006_peiqian3.lbp.0001": "audio/voice/scn_0006_peiqian3/lbp/0001.mp3",
        "voice.scn_0006_peiqian3.narr.0001": "audio/voice/scn_0006_peiqian3/narr/0001.mp3",
        "voice.scn_0006_peiqian3.pq.0001": "audio/voice/scn_0006_peiqian3/pq/0001.mp3",
        "voice.scn_0006_peiqian3.pq.0002": "audio/voice/scn_0006_peiqian3/pq/0002.mp3",
        "voice.scn_0006_peiqian3.pq.0003": "audio/voice/scn_0006_peiqian3/pq/0003.mp3",
        "voice.scn_0006_peiqian3.pq.0004": "audio/voice/scn_0006_peiqian3/pq/0004.mp3",
        "voice.scn_0006_peiqian3.pq.0005": "audio/voice/scn_0006_peiqian3/pq/0005.mp3",
        "voice.scn_0006_peiqian3.pq.0006": "audio/voice/scn_0006_peiqian3/pq/0006.mp3",
        "voice.scn_0006_peiqian3.pq.0007": "audio/voice/scn_0006_peiqian3/pq/0007.mp3",
        "voice.scn_0006_peiqian3.pq.0008": "audio/voice/scn_0006_peiqian3/pq/0008.mp3",
        "voice.scn_0007_chengpinan.cds.0001": "audio/voice/scn_0007_chengpinan/cds/0001.mp3",
        "voice.scn_0008_chengpinan2.cpy.0001": "audio/voice/scn_0008_chengpinan2/cpy/0001.mp3",
        "voice.scn_0008_chengpinan2.cpy.0002": "audio/voice/scn_0008_chengpinan2/cpy/0002.mp3",
        "voice.scn_0009_chengpinan3.cpy.0001": "audio/voice/scn_0009_chengpinan3/cpy/0001.mp3",
        "voice.scn_0010_huyuanko.cpy.0001": "audio/voice/scn_0010_huyuanko/cpy/0001.mp3",
        "voice.scn_0010_huyuanko.cpy.0002": "audio/voice/scn_0010_huyuanko/cpy/0002.mp3",
        "voice.scn_0010_huyuanko.cpy.0003": "audio/voice/scn_0010_huyuanko/cpy/0003.mp3",
        "voice.scn_0010_huyuanko.lbp.0001": "audio/voice/scn_0010_huyuanko/lbp/0001.mp3",
        "voice.scn_0010_huyuanko.lh.0001": "audio/voice/scn_0010_huyuanko/lh/0001.mp3",
        "voice.scn_0010_huyuanko.mxd.0001": "audio/voice/scn_0010_huyuanko/mxd/0001.mp3",
        "voice.scn_0011_da_uei.cds.0001": "audio/voice/scn_0011_da_uei/cds/0001.mp3",
        "voice.scn_0011_da_uei.cds.0002": "audio/voice/scn_0011_da_uei/cds/0002.mp3",
        "voice.scn_0011_da_uei.cds.0003": "audio/voice/scn_0011_da_uei/cds/0003.mp3",
        "voice.scn_0011_da_uei.cds.0004": "audio/voice/scn_0011_da_uei/cds/0004.mp3",
        "voice.scn_0011_da_uei.cds.0005": "audio/voice/scn_0011_da_uei/cds/0005.mp3",
        "voice.scn_0011_da_uei.cpy.0001": "audio/voice/scn_0011_da_uei/cpy/0001.mp3",
        "voice.scn_0011_da_uei.cpy.0002": "audio/voice/scn_0011_da_uei/cpy/0002.mp3",
        "voice.scn_0011_da_uei.cpy.0003": "audio/voice/scn_0011_da_uei/cpy/0003.mp3",
    }
    def voice_id(voice_key):
        """
        Returns the voice file path for a given voice ID.
        """
        path = VOICE_INDEX.get(voice_key)
        if path is None:
            raise Exception("Unknown voice id: %r" % (voice_key,))
        return path

